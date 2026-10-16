from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Customer, Order

from django.db import transaction
from django.contrib import messages


def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:4]

    if not featured_products.exists():
        featured_products = Product.objects.all()[:4]

    categories = (
        Product.objects
        .values_list('category', flat=True)
        .distinct()
    )

    context = {
        'featured_products': featured_products,
        'categories': categories,
    }

    return render(request, 'shop/home.html', context)


def products(request):
    all_products = Product.objects.all().order_by('name')

    context = {
        'products': all_products,
    }

    return render(request, 'shop/products.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
def products(request):
    category = request.GET.get('category')

    all_products = Product.objects.all().order_by('name')

    if category:
        all_products = all_products.filter(category=category)

    context = {
        'products': all_products,
        'selected_category': category,
    }

    return render(request, 'shop/products.html', context)

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.quantity > 0:
        cart = request.session.get('cart', {})
        product_id = str(product.id)

        current_quantity = cart.get(product_id, 0)

        if current_quantity < product.quantity:
            cart[product_id] = current_quantity + 1

        request.session['cart'] = cart

    return redirect('cart')


def cart(request):
    cart_data = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():
        try:
            product = Product.objects.get(pk=int(product_id))
        except (Product.DoesNotExist, ValueError):
            continue

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })


def update_cart(request, pk):
    if request.method == 'POST':
        cart_data = request.session.get('cart', {})
        product_id = str(pk)

        if product_id in cart_data:
            try:
                quantity = int(request.POST.get('quantity', 1))
                product = get_object_or_404(Product, pk=pk)

                if 1 <= quantity <= product.quantity:
                    cart_data[product_id] = quantity
                elif quantity <= 0:
                    del cart_data[product_id]

                request.session['cart'] = cart_data
            except (ValueError, TypeError):
                pass

    return redirect('cart')


def remove_from_cart(request, pk):
    if request.method == 'POST':
        cart_data = request.session.get('cart', {})
        cart_data.pop(str(pk), None)
        request.session['cart'] = cart_data

    return redirect('cart')

def checkout(request):
    cart_data = request.session.get('cart', {})

    if not cart_data:
        messages.warning(request, 'তোমার কার্ট খালি।')
        return redirect('cart')

    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, pk=int(product_id))

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()

        if not name or not phone or not address:
            messages.error(request, 'সব তথ্য পূরণ করো।')
        else:
            try:
                with transaction.atomic():
                    customer = Customer.objects.create(
                        name=name,
                        phone=phone,
                        address=address,
                    )

                    for item in cart_items:
                        product = Product.objects.select_for_update().get(
                            pk=item['product'].pk
                        )
                        quantity = item['quantity']

                        if quantity < 1 or product.quantity < quantity:
                            raise ValueError(
                                f'{product.name} বইটির পর্যাপ্ত স্টক নেই।'
                            )

                        product.quantity -= quantity
                        product.save(update_fields=['quantity'])

                        Order.objects.create(
                            customer=customer,
                            product=product,
                            quantity=quantity,
                            total_price=product.price * quantity,
                        )

                request.session['cart'] = {}
                request.session['last_order_total'] = str(total)

                return redirect('order_success')

            except (ValueError, Product.DoesNotExist):
                messages.error(
                    request,
                    'স্টক পরিবর্তন হয়েছে। কার্ট যাচাই করে আবার চেষ্টা করো।'
                )
                return redirect('cart')

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })


def order_success(request):
    total = request.session.pop('last_order_total', None)

    if total is None:
        return redirect('home')

    return render(request, 'shop/order_success.html', {
        'total': total,
    })

def products(request):
    search_query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    all_products = Product.objects.all().order_by('name')

    if search_query:
        all_products = all_products.filter(name__icontains=search_query)

    if category:
        all_products = all_products.filter(category=category)

    categories = (
        Product.objects
        .values_list('category', flat=True)
        .distinct()
        .order_by('category')
    )

    context = {
        'products': all_products,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category,
    }

    return render(request, 'shop/products.html', context)

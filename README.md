# Single Vendor E-commerce Website

A simple and responsive single-vendor e-commerce website built with Django, HTML, CSS, JavaScript, Bootstrap 5, and SQLite. This project is developed as a learning assignment to practice Django models, views, URL routing, templates, forms, database operations, and basic frontend development.

## YouTube Video

Watch the project video:

[▶ Watch on YouTube](https://youtu.be/jnTNK2EhKqk)


## Project Overview

The Single Vendor E-commerce Website allows customers to browse products, view product details, manage a shopping cart, and place orders through a simple checkout form.

Products are managed through the Django Admin Panel, and customer orders are stored in the SQLite database.

The project focuses on simplicity, functionality, and beginner-friendly implementation.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript
- **CSS Framework:** Bootstrap 5
- **Database:** SQLite
- **Template Engine:** Django Templates
- **Version Control:** Git and GitHub

## Features

### Home Page
- Shop name and navigation bar
- Bootstrap banner section
- Product categories
- Featured products
- Footer section

### Product Management
- Display products from the Django database
- Show product images, names, prices, and short descriptions
- View individual product details
- Display available product quantities

### Shopping Cart
- Add products to the cart
- Increase or decrease product quantities
- Remove products from the cart
- Calculate the total price automatically

### Checkout and Orders
- Simple checkout form
- Collect customer name, phone number, and address
- Save customer and order information in the database
- Display an order success message after placing an order

### Django Admin Panel
- Add new products
- Update existing products
- Manage product prices, images, descriptions, and stock quantities
- View customer and order records

### Responsive Design
- Bootstrap navbar, cards, buttons, forms, and grid system
- Simple custom CSS styling
- Responsive layout for desktop and mobile devices

## Required Pages

1. Home Page
2. Products Page
3. Product Details Page
4. Shopping Cart Page
5. Checkout Page
6. Order Success Page

## Project Structure

The project will follow a simple Django structure similar to the following:

```text
single-vendor-ecommerce/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── shop/
│   ├── migrations/
│   ├── templates/
│   │   └── shop/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── products.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── checkout.html
│   │       └── order_success.html
│   ├── static/
│   │   └── shop/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── js/
│   │           └── script.js
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── db.sqlite3
```

*Note: This is the planned structure. The actual structure may vary slightly during development.*

## Database Models

The project will include at least the following three models:

### Product
Stores product information, including:
- Product name
- Price
- Description
- Image
- Available quantity

### Customer
Stores customer information, including:
- Name
- Phone number
- Address

### Order
Stores order information, including:
- Customer
- Product
- Quantity
- Total price
- Order date

Additional fields or models may be introduced when necessary to support the shopping cart and order functionality.

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/single-vendor-ecommerce.git
cd single-vendor-ecommerce
```

Replace `YOUR-USERNAME` with the actual GitHub username.

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an administrator account.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open the following URL in your browser:

http://127.0.0.1:8000/

To access the Django Admin Panel, visit:

http://127.0.0.1:8000/admin/

Log in using your superuser credentials and add products through the admin interface.

## How It Works

The main shopping workflow is:

**Browse Products → View Product Details → Add to Cart → Manage Cart → Checkout → Place Order → Order Success**

1. Customers browse available products on the website.
2. They view product details and add products to the shopping cart.
3. They update quantities or remove products from the cart.
4. The website calculates the total price.
5. Customers enter their name, phone number, and address on the checkout page.
6. After submitting the order, the customer and order information are saved in the database.
7. The website displays an order success page.

## JavaScript Functionality

JavaScript will be used for simple interactive features, such as quantity controls and total-price updates.

Django will handle database operations, URL routing, server-side validation, and order processing.

## Learning Objectives

This project helps practice:

- Creating Django projects and applications
- Defining models and database relationships
- Performing database migrations
- Using Django views and URL routing
- Rendering dynamic content with Django Templates
- Processing HTML forms
- Managing products through Django Admin
- Implementing a basic shopping cart
- Saving customer and order information
- Using Bootstrap for responsive layouts
- Adding simple JavaScript interactions
- Managing source code with Git and GitHub

## Future Improvements

Possible improvements include:

- Product search
- Product category filtering
- User registration and login
- Product discounts
- Product ratings
- Customer order history

These features may be added after completing the mandatory assignment requirements.

## Assignment Submission

This project is developed as a Django e-commerce assignment using the required technologies and SQLite database.

The source code, templates, static files, migrations, dependency list, and documentation will be maintained in this GitHub repository.

## Author

**Your Name**

GitHub: https://github.com/rabeyasumi

---

*Built with Django, Bootstrap, and a focus on learning the fundamentals of web development.*

# 🛍️ Indian Clothing Store - Python Flask E-Commerce Website

A comprehensive clothing e-commerce platform built with Python Flask, featuring age-based product categories tailored for the Indian market.

## 🌟 Features

### Age-Based Categories
- **Infant & Toddler (0-3 years)** - Soft cotton wear for babies
- **Kids Wear (4-12 years)** - Durable and playful clothing
- **Teenage Wear (13-19 years)** - Trendy outfits for teens
- **Young Adults (20-35 years)** - Modern fashion
- **Adults (36-55 years)** - Elegant and comfortable wear
- **Senior Wear (56+ years)** - Easy-to-wear comfortable clothing
- **Ethnic Wear** - Traditional Indian clothing (Sarees, Kurtas, Sherwanis)
- **Western Wear** - Contemporary fashion

### E-Commerce Features
- ✅ User Registration & Login
- ✅ Product Browsing by Age Categories
- ✅ Detailed Product Pages with Multiple Sizes
- ✅ Shopping Cart Management
- ✅ Secure Checkout Process
- ✅ Order History & Tracking
- ✅ Product Search Functionality
- ✅ Multiple Payment Methods (COD, UPI, Cards, Net Banking, Wallets)
- ✅ Free Delivery on orders above ₹999
- ✅ Rating & Review System
- ✅ Discount & Offer Display

### Indian Market Features
- 🇮🇳 Indian Rupee (₹) Pricing
- 🇮🇳 Traditional & Western Wear Mix
- 🇮🇳 Cash on Delivery (COD) Support
- 🇮🇳 UPI & Mobile Wallet Integration
- 🇮🇳 Age-appropriate sizing (Indian standards)
- 🇮🇳 Festival & Wedding Collections

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Navigate to the project directory:**
```powershell
cd clothing-store
```

2. **Install dependencies:**
```powershell
pip install -r requirements.txt
```

3. **Initialize the database with seed data:**
```powershell
python seed_data.py
```

4. **Run the application:**
```powershell
python app.py
```

5. **Open your browser and visit:**
```
http://localhost:5000
```

## 📁 Project Structure

```
clothing-store/
├── app.py                  # Main Flask application
├── seed_data.py           # Database seeding script
├── requirements.txt       # Python dependencies
├── clothing_store.db      # SQLite database (auto-generated)
└── templates/             # HTML templates
    ├── base.html          # Base template with navigation
    ├── index.html         # Homepage with featured products
    ├── category.html      # Category product listing
    ├── product_detail.html # Individual product page
    ├── cart.html          # Shopping cart
    ├── checkout.html      # Checkout page
    ├── order_success.html # Order confirmation
    ├── my_orders.html     # User order history
    ├── login.html         # User login
    ├── register.html      # User registration
    └── search_results.html # Search results page
```

## 💾 Database Schema

### Tables
- **User** - Customer accounts
- **Category** - Age-based product categories
- **Product** - Clothing items with details
- **Cart** - Shopping cart items
- **Order** - Order information
- **OrderItem** - Individual items in orders

## 🛒 Sample Products Included

The seed data includes **30+ realistic products** across all age groups:

### Infant & Toddler
- Baby Cotton Romper Sets
- Infant Onesies
- Toddler Frocks

### Kids
- T-Shirt & Shorts Sets
- Palazzo Kurti Sets for Girls
- Denim Jeans for Boys

### Teenage
- Crop Tops with Jeans
- Hoodies & Track Pants
- Indo-Western Kurtis

### Young Adults
- Formal Shirts
- Designer Sarees
- Casual Chinos
- Palazzo Suits

### Adults
- Cotton Kurta Pajama
- Cotton Salwar Kameez
- Formal Trousers

### Seniors
- Comfort Kurtas
- Cotton Nighties
- Elastic Waist Pants

### Ethnic Collection
- Banarasi Silk Sarees
- Designer Sherwanis
- Anarkali Suits

### Western Collection
- Party Dresses
- Denim Jackets

## 🎯 Key Features Details

### Payment Methods Supported
- Cash on Delivery (COD)
- UPI / BHIM
- Credit/Debit Cards
- Net Banking
- Mobile Wallets (Paytm, PhonePe, Google Pay, etc.)

### Shipping
- Free delivery on orders ≥ ₹999
- ₹50 delivery charge for orders < ₹999

### Product Information
- Multiple sizes available
- Color variants
- Material details
- Brand information
- Stock availability
- Customer ratings

## 🔐 User Authentication

- Secure password hashing using Werkzeug
- Session-based authentication
- Protected routes for cart and checkout

## 📱 Responsive Design

The website features a modern, responsive design that works on:
- Desktop computers
- Tablets
- Mobile phones

## 🎨 Design Highlights

- Gradient color schemes
- Age-appropriate category cards
- Clean product cards with hover effects
- Intuitive navigation
- Professional checkout flow
- Order confirmation pages

## 🛠️ Technology Stack

- **Backend:** Python Flask 3.0
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** HTML5, CSS3, Jinja2 Templates
- **Authentication:** Werkzeug Security
- **Architecture:** MVC Pattern

## 📊 Database Features

- Automatic table creation
- Relationship management (Foreign Keys)
- Transaction support
- Data validation
- Timestamp tracking

## 🚧 Future Enhancements

Potential additions:
- Product image uploads
- Customer reviews & ratings
- Wishlist functionality
- Email notifications
- SMS order updates
- Payment gateway integration (Razorpay, Paytm)
- Admin dashboard
- Inventory management
- Sales analytics
- Coupon codes & discounts
- Size guide
- Product recommendations

## 📝 Notes

- This is a demonstration project with realistic Indian clothing products
- Database is SQLite (suitable for development; use PostgreSQL/MySQL for production)
- Payment integration is simulated (not connected to actual payment gateways)
- Product images are represented by emoji icons

## 🤝 Support

For questions or support, please create an issue in the repository.

## 📄 License

This project is created for educational purposes.

---

**Made with ❤️ for the Indian Clothing Market** 🇮🇳

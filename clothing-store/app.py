"""
Indian Clothing Store - Flask Application
A comprehensive e-commerce platform for selling clothes based on age categories
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clothing_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    orders = db.relationship('Order', backref='user', lazy=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age_group = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    stock = db.Column(db.Integer, default=0)
    size = db.Column(db.String(50))  # S, M, L, XL, XXL, or age-based sizes
    color = db.Column(db.String(50))
    material = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    image_url = db.Column(db.String(500))
    is_featured = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    size = db.Column(db.String(50))
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    product = db.relationship('Product', backref='cart_items')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')  # Pending, Confirmed, Shipped, Delivered
    payment_method = db.Column(db.String(50))
    shipping_address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(50))
    product = db.relationship('Product')

# Routes
@app.route('/')
def index():
    featured_products = Product.query.filter_by(is_featured=True).limit(8).all()
    categories = Category.query.all()
    return render_template('index.html', featured_products=featured_products, categories=categories)

@app.route('/category/<int:category_id>')
def category_products(category_id):
    category = Category.query.get_or_404(category_id)
    products = Product.query.filter_by(category_id=category_id).all()
    return render_template('category.html', category=category, products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    related_products = Product.query.filter_by(category_id=product.category_id).filter(Product.id != product_id).limit(4).all()
    return render_template('product_detail.html', product=product, related_products=related_products)

@app.route('/cart')
def cart():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    cart_items = Cart.query.filter_by(user_id=session['user_id']).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Please login first'}), 401
    
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    size = data.get('size')
    
    # Check if item already in cart
    existing_item = Cart.query.filter_by(
        user_id=session['user_id'],
        product_id=product_id,
        size=size
    ).first()
    
    if existing_item:
        existing_item.quantity += quantity
    else:
        cart_item = Cart(
            user_id=session['user_id'],
            product_id=product_id,
            quantity=quantity,
            size=size
        )
        db.session.add(cart_item)
    
    db.session.commit()
    return jsonify({'success': True, 'message': 'Item added to cart'})

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        
        # Check if user already exists
        if User.query.filter_by(email=data['email']).first():
            return render_template('register.html', error='Email already registered')
        
        hashed_password = generate_password_hash(data['password'])
        user = User(
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            phone=data.get('phone'),
            address=data.get('address')
        )
        
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        session['user_name'] = user.name
        return redirect(url_for('index'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        cart_items = Cart.query.filter_by(user_id=session['user_id']).all()
        
        if not cart_items:
            return redirect(url_for('cart'))
        
        total = sum(item.product.price * item.quantity for item in cart_items)
        
        order = Order(
            user_id=session['user_id'],
            total_amount=total,
            payment_method=request.form.get('payment_method'),
            shipping_address=request.form.get('shipping_address')
        )
        db.session.add(order)
        db.session.flush()
        
        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.product.price,
                size=item.size
            )
            db.session.add(order_item)
            
            # Update stock
            product = Product.query.get(item.product_id)
            product.stock -= item.quantity
        
        # Clear cart
        Cart.query.filter_by(user_id=session['user_id']).delete()
        
        db.session.commit()
        
        return redirect(url_for('order_success', order_id=order.id))
    
    cart_items = Cart.query.filter_by(user_id=session['user_id']).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    user = User.query.get(session['user_id'])
    
    return render_template('checkout.html', cart_items=cart_items, total=total, user=user)

@app.route('/order_success/<int:order_id>')
def order_success(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order_success.html', order=order)

@app.route('/my_orders')
def my_orders():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    orders = Order.query.filter_by(user_id=session['user_id']).order_by(Order.created_at.desc()).all()
    return render_template('my_orders.html', orders=orders)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    products = Product.query.filter(Product.name.contains(query) | Product.description.contains(query)).all()
    return render_template('search_results.html', products=products, query=query)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)

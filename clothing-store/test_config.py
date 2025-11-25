"""
Test configuration and utilities
"""

import os
import sys

# Test configuration
class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = 'test-secret-key-12345'
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Test data generators
def create_test_user(username='testuser', email='test@example.com', password='testpass123'):
    """Helper function to create test user"""
    from app import User
    user = User(
        username=username,
        email=email,
        phone='9876543210',
        address='123 Test Street, Mumbai'
    )
    user.set_password(password)
    return user

def create_test_product(name='Test Product', price=999.00, category='Men', stock=50):
    """Helper function to create test product"""
    from app import Product
    product = Product(
        name=name,
        description=f'Description for {name}',
        price=price,
        category=category,
        age_group='Adults (18-60)',
        stock=stock,
        image_url='/static/images/test.jpg'
    )
    return product

def create_test_order(user_id, total_amount=1000.00, status='Pending'):
    """Helper function to create test order"""
    from app import Order
    order = Order(
        user_id=user_id,
        total_amount=total_amount,
        status=status,
        shipping_address='123 Test Street, Mumbai'
    )
    return order

# Test categories for Indian market
TEST_CATEGORIES = ['Men', 'Women', 'Kids']

# Test age groups
TEST_AGE_GROUPS = [
    'Infants (0-2)',
    'Toddlers (2-5)',
    'Children (5-12)',
    'Teens (13-17)',
    'Adults (18-60)',
    'Seniors (60+)'
]

# Test products for Indian market
TEST_PRODUCTS = [
    {
        'name': 'Cotton Kurta',
        'price': 799.00,
        'category': 'Men',
        'age_group': 'Adults (18-60)'
    },
    {
        'name': 'Silk Saree',
        'price': 2499.00,
        'category': 'Women',
        'age_group': 'Adults (18-60)'
    },
    {
        'name': 'Kids Ethnic Wear',
        'price': 599.00,
        'category': 'Kids',
        'age_group': 'Children (5-12)'
    },
    {
        'name': 'Formal Shirt',
        'price': 1299.00,
        'category': 'Men',
        'age_group': 'Adults (18-60)'
    },
    {
        'name': 'Kurti Set',
        'price': 1099.00,
        'category': 'Women',
        'age_group': 'Adults (18-60)'
    }
]

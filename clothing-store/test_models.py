"""
Unit tests specifically for database models
Tests Model validations, relationships, and constraints
"""

import unittest
from app import app, db, Product, User, Order, OrderItem, Cart
from datetime import datetime

class TestUserModel(unittest.TestCase):
    """Test User model"""
    
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app_context = app.app_context()
        cls.app_context.push()
        db.create_all()
    
    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def setUp(self):
        db.session.query(User).delete()
        db.session.commit()
    
    def test_user_creation(self):
        """Test creating a user"""
        user = User(
            username='testuser',
            email='test@example.com',
            phone='9876543210',
            address='Test Address'
        )
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        self.assertIsNotNone(user.id)
        self.assertEqual(user.username, 'testuser')
    
    def test_password_verification(self):
        """Test password hashing and verification"""
        user = User(username='user1', email='user1@test.com')
        user.set_password('mypassword')
        
        self.assertTrue(user.check_password('mypassword'))
        self.assertFalse(user.check_password('wrongpassword'))
    
    def test_user_repr(self):
        """Test user string representation"""
        user = User(username='testuser', email='test@example.com')
        self.assertIn('testuser', repr(user))


class TestProductModel(unittest.TestCase):
    """Test Product model"""
    
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app_context = app.app_context()
        cls.app_context.push()
        db.create_all()
    
    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def setUp(self):
        db.session.query(Product).delete()
        db.session.commit()
    
    def test_product_creation(self):
        """Test creating a product"""
        product = Product(
            name='Test Product',
            description='Test Description',
            price=999.99,
            category='Men',
            age_group='Adults (18-60)',
            stock=100,
            image_url='/static/test.jpg'
        )
        db.session.add(product)
        db.session.commit()
        
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 999.99)
    
    def test_product_default_values(self):
        """Test product default values"""
        product = Product(
            name='Test Product',
            price=100.00,
            category='Women'
        )
        db.session.add(product)
        db.session.commit()
        
        self.assertEqual(product.stock, 0)
    
    def test_product_repr(self):
        """Test product string representation"""
        product = Product(name='Test Product', price=100.00, category='Kids')
        self.assertIn('Test Product', repr(product))


class TestCartModel(unittest.TestCase):
    """Test Cart model"""
    
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app_context = app.app_context()
        cls.app_context.push()
        db.create_all()
    
    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def setUp(self):
        db.session.query(Cart).delete()
        db.session.query(Product).delete()
        db.session.query(User).delete()
        db.session.commit()
    
    def test_cart_item_creation(self):
        """Test creating a cart item"""
        user = User(username='user1', email='user1@test.com')
        user.set_password('pass')
        product = Product(name='Product1', price=100.00, category='Men')
        
        db.session.add(user)
        db.session.add(product)
        db.session.commit()
        
        cart_item = Cart(user_id=user.id, product_id=product.id, quantity=2)
        db.session.add(cart_item)
        db.session.commit()
        
        self.assertIsNotNone(cart_item.id)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.user_id, user.id)
        self.assertEqual(cart_item.product_id, product.id)
    
    def test_cart_item_relationship(self):
        """Test cart item relationships with user and product"""
        user = User(username='user1', email='user1@test.com')
        user.set_password('pass')
        product = Product(name='Product1', price=100.00, category='Men')
        
        db.session.add(user)
        db.session.add(product)
        db.session.commit()
        
        cart_item = Cart(user_id=user.id, product_id=product.id, quantity=1)
        db.session.add(cart_item)
        db.session.commit()
        
        self.assertEqual(cart_item.user.username, 'user1')
        self.assertEqual(cart_item.product.name, 'Product1')


class TestOrderModel(unittest.TestCase):
    """Test Order and OrderItem models"""
    
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app_context = app.app_context()
        cls.app_context.push()
        db.create_all()
    
    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def setUp(self):
        db.session.query(OrderItem).delete()
        db.session.query(Order).delete()
        db.session.query(Product).delete()
        db.session.query(User).delete()
        db.session.commit()
    
    def test_order_creation(self):
        """Test creating an order"""
        user = User(username='user1', email='user1@test.com')
        user.set_password('pass')
        db.session.add(user)
        db.session.commit()
        
        order = Order(
            user_id=user.id,
            total_amount=1500.00,
            status='Pending',
            shipping_address='123 Test St'
        )
        db.session.add(order)
        db.session.commit()
        
        self.assertIsNotNone(order.id)
        self.assertEqual(order.total_amount, 1500.00)
        self.assertEqual(order.status, 'Pending')
        self.assertIsNotNone(order.created_at)
    
    def test_order_item_creation(self):
        """Test creating order items"""
        user = User(username='user1', email='user1@test.com')
        user.set_password('pass')
        product = Product(name='Product1', price=100.00, category='Men')
        
        db.session.add(user)
        db.session.add(product)
        db.session.commit()
        
        order = Order(user_id=user.id, total_amount=200.00, status='Pending')
        db.session.add(order)
        db.session.commit()
        
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=2,
            price=100.00
        )
        db.session.add(order_item)
        db.session.commit()
        
        self.assertIsNotNone(order_item.id)
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.price, 100.00)
    
    def test_order_items_relationship(self):
        """Test order has relationship with items"""
        user = User(username='user1', email='user1@test.com')
        user.set_password('pass')
        product = Product(name='Product1', price=100.00, category='Men')
        
        db.session.add(user)
        db.session.add(product)
        db.session.commit()
        
        order = Order(user_id=user.id, total_amount=200.00, status='Pending')
        db.session.add(order)
        db.session.commit()
        
        order_item1 = OrderItem(order_id=order.id, product_id=product.id, quantity=1, price=100.00)
        order_item2 = OrderItem(order_id=order.id, product_id=product.id, quantity=1, price=100.00)
        
        db.session.add(order_item1)
        db.session.add(order_item2)
        db.session.commit()
        
        self.assertEqual(len(order.items), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)

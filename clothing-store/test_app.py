"""
Comprehensive unit tests for the Clothing Store application
Tests cover: Models, Routes, Authentication, Cart, Orders, and Database operations
"""

import unittest
import os
import json
from datetime import datetime
from app import app, db, Product, User, Order, OrderItem, Cart, Category

class TestConfig:
    """Test configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = 'test-secret-key'
    WTF_CSRF_ENABLED = False

class BaseTestCase(unittest.TestCase):
    """Base test case with common setup and teardown"""
    
    def setUp(self):
        """Set up test client and initialize database"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SECRET_KEY'] = 'test-secret-key'
        
        self.app = app
        self.client = app.test_client()
        
        with app.app_context():
            db.create_all()
            self._seed_test_data()
    
    def tearDown(self):
        """Clean up after tests"""
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def _seed_test_data(self):
        """Seed database with test data"""
        # Create test user
        user = User(
            username='testuser',
            email='test@example.com',
            phone='9876543210',
            address='123 Test Street, Mumbai'
        )
        user.set_password('testpass123')
        db.session.add(user)
        
        # Create admin user
        admin = User(
            username='admin',
            email='admin@example.com',
            phone='9999999999',
            address='Admin Office',
            is_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        
        # Create test products
        products = [
            Product(
                name='Cotton Kurta',
                description='Traditional Indian kurta for men',
                price=799.00,
                category='Men',
                age_group='Adults (18-60)',
                stock=50,
                image_url='/static/images/mens-kurta.jpg'
            ),
            Product(
                name='Silk Saree',
                description='Elegant silk saree for women',
                price=2499.00,
                category='Women',
                age_group='Adults (18-60)',
                stock=30,
                image_url='/static/images/womens-saree.jpg'
            ),
            Product(
                name='Kids T-Shirt',
                description='Colorful t-shirt for kids',
                price=299.00,
                category='Kids',
                age_group='Children (5-12)',
                stock=100,
                image_url='/static/images/kids-tshirt.jpg'
            ),
            Product(
                name='Baby Romper',
                description='Soft cotton romper for babies',
                price=399.00,
                category='Kids',
                age_group='Infants (0-2)',
                stock=75,
                image_url='/static/images/baby-romper.jpg'
            ),
            Product(
                name='Senior Comfortable Shirt',
                description='Easy-wear shirt for seniors',
                price=899.00,
                category='Men',
                age_group='Seniors (60+)',
                stock=40,
                image_url='/static/images/senior-shirt.jpg'
            )
        ]
        
        for product in products:
            db.session.add(product)
        
        db.session.commit()
    
    def login(self, username='testuser', password='testpass123'):
        """Helper method to log in a user"""
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)
    
    def logout(self):
        """Helper method to log out"""
        return self.client.get('/logout', follow_redirects=True)


class TestModels(BaseTestCase):
    """Test database models"""
    
    def test_user_model_creation(self):
        """Test user model can be created"""
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.email, 'test@example.com')
            self.assertEqual(user.phone, '9876543210')
    
    def test_user_password_hashing(self):
        """Test password is properly hashed"""
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertTrue(user.check_password('testpass123'))
            self.assertFalse(user.check_password('wrongpassword'))
            self.assertNotEqual(user.password_hash, 'testpass123')
    
    def test_admin_user_flag(self):
        """Test admin user flag"""
        with app.app_context():
            admin = User.query.filter_by(username='admin').first()
            regular_user = User.query.filter_by(username='testuser').first()
            self.assertTrue(admin.is_admin)
            self.assertFalse(regular_user.is_admin)
    
    def test_product_model_creation(self):
        """Test product model can be created"""
        with app.app_context():
            product = Product.query.filter_by(name='Cotton Kurta').first()
            self.assertIsNotNone(product)
            self.assertEqual(product.price, 799.00)
            self.assertEqual(product.category, 'Men')
            self.assertEqual(product.stock, 50)
    
    def test_product_age_groups(self):
        """Test products have correct age groups"""
        with app.app_context():
            infant_product = Product.query.filter_by(age_group='Infants (0-2)').first()
            senior_product = Product.query.filter_by(age_group='Seniors (60+)').first()
            self.assertIsNotNone(infant_product)
            self.assertIsNotNone(senior_product)
    
    def test_cart_item_creation(self):
        """Test cart item can be created"""
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=2)
            db.session.add(cart_item)
            db.session.commit()
            
            saved_item = Cart.query.filter_by(user_id=user.id).first()
            self.assertIsNotNone(saved_item)
            self.assertEqual(saved_item.quantity, 2)
    
    def test_order_creation(self):
        """Test order can be created"""
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            
            order = Order(
                user_id=user.id,
                total_amount=1500.00,
                status='Pending',
                shipping_address='123 Test Street'
            )
            db.session.add(order)
            db.session.commit()
            
            saved_order = Order.query.filter_by(user_id=user.id).first()
            self.assertIsNotNone(saved_order)
            self.assertEqual(saved_order.total_amount, 1500.00)
            self.assertEqual(saved_order.status, 'Pending')
    
    def test_order_item_relationship(self):
        """Test order items are linked to orders"""
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            
            order = Order(user_id=user.id, total_amount=799.00, status='Pending')
            db.session.add(order)
            db.session.commit()
            
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=1,
                price=product.price
            )
            db.session.add(order_item)
            db.session.commit()
            
            self.assertEqual(len(order.items), 1)
            self.assertEqual(order.items[0].product.name, product.name)


class TestAuthentication(BaseTestCase):
    """Test authentication and user management"""
    
    def test_login_page_loads(self):
        """Test login page is accessible"""
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)
    
    def test_register_page_loads(self):
        """Test register page is accessible"""
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)
    
    def test_user_registration(self):
        """Test new user can register"""
        response = self.client.post('/register', data=dict(
            username='newuser',
            email='newuser@example.com',
            password='newpass123',
            phone='9876543211',
            address='456 New Street, Delhi'
        ), follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        
        with app.app_context():
            user = User.query.filter_by(username='newuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.email, 'newuser@example.com')
    
    def test_duplicate_username_registration(self):
        """Test duplicate username is rejected"""
        response = self.client.post('/register', data=dict(
            username='testuser',  # Already exists
            email='another@example.com',
            password='pass123',
            phone='9876543212',
            address='789 Street'
        ), follow_redirects=True)
        
        self.assertIn(b'Username already exists', response.data)
    
    def test_successful_login(self):
        """Test user can log in with correct credentials"""
        response = self.login()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'testuser', response.data)
    
    def test_failed_login_wrong_password(self):
        """Test login fails with wrong password"""
        response = self.login(password='wrongpassword')
        self.assertIn(b'Invalid username or password', response.data)
    
    def test_failed_login_nonexistent_user(self):
        """Test login fails for non-existent user"""
        response = self.login(username='nonexistent', password='pass123')
        self.assertIn(b'Invalid username or password', response.data)
    
    def test_logout(self):
        """Test user can log out"""
        self.login()
        response = self.logout()
        self.assertEqual(response.status_code, 200)


class TestProductRoutes(BaseTestCase):
    """Test product-related routes"""
    
    def test_home_page_loads(self):
        """Test home page displays products"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cotton Kurta', response.data)
        self.assertIn(b'Silk Saree', response.data)
    
    def test_product_detail_page(self):
        """Test product detail page loads"""
        with app.app_context():
            product = Product.query.first()
            response = self.client.get(f'/product/{product.id}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(product.name.encode(), response.data)
    
    def test_category_page_men(self):
        """Test men's category page"""
        response = self.client.get('/category/Men')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cotton Kurta', response.data)
    
    def test_category_page_women(self):
        """Test women's category page"""
        response = self.client.get('/category/Women')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Silk Saree', response.data)
    
    def test_category_page_kids(self):
        """Test kids' category page"""
        response = self.client.get('/category/Kids')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kids T-Shirt', response.data)
    
    def test_search_functionality(self):
        """Test product search works"""
        response = self.client.get('/search?q=kurta')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cotton Kurta', response.data)
    
    def test_search_no_results(self):
        """Test search with no matching products"""
        response = self.client.get('/search?q=nonexistentproduct')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No products found', response.data)


class TestCartFunctionality(BaseTestCase):
    """Test shopping cart functionality"""
    
    def test_add_to_cart_requires_login(self):
        """Test adding to cart requires authentication"""
        response = self.client.post('/add_to_cart/1', follow_redirects=True)
        self.assertIn(b'Login', response.data)
    
    def test_add_to_cart_authenticated(self):
        """Test authenticated user can add to cart"""
        self.login()
        with app.app_context():
            product = Product.query.first()
            response = self.client.post(f'/add_to_cart/{product.id}', 
                                       data=dict(quantity=2),
                                       follow_redirects=True)
            
            self.assertEqual(response.status_code, 200)
            
            user = User.query.filter_by(username='testuser').first()
            cart_item = Cart.query.filter_by(user_id=user.id, product_id=product.id).first()
            self.assertIsNotNone(cart_item)
            self.assertEqual(cart_item.quantity, 2)
    
    def test_view_cart_empty(self):
        """Test viewing empty cart"""
        self.login()
        response = self.client.get('/cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your cart is empty', response.data)
    
    def test_view_cart_with_items(self):
        """Test viewing cart with items"""
        self.login()
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=2)
            db.session.add(cart_item)
            db.session.commit()
        
        response = self.client.get('/cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(product.name.encode(), response.data)
    
    def test_update_cart_quantity(self):
        """Test updating cart item quantity"""
        self.login()
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=2)
            db.session.add(cart_item)
            db.session.commit()
            cart_item_id = cart_item.id
        
        response = self.client.post(f'/update_cart/{cart_item_id}', 
                                   data=dict(quantity=5),
                                   follow_redirects=True)
        
        with app.app_context():
            updated_item = Cart.query.get(cart_item_id)
            self.assertEqual(updated_item.quantity, 5)
    
    def test_remove_from_cart(self):
        """Test removing item from cart"""
        self.login()
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=2)
            db.session.add(cart_item)
            db.session.commit()
            cart_item_id = cart_item.id
        
        response = self.client.post(f'/remove_from_cart/{cart_item_id}', 
                                   follow_redirects=True)
        
        with app.app_context():
            removed_item = Cart.query.get(cart_item_id)
            self.assertIsNone(removed_item)
    
    def test_cart_total_calculation(self):
        """Test cart total is calculated correctly"""
        self.login()
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product1 = Product.query.filter_by(name='Cotton Kurta').first()
            product2 = Product.query.filter_by(name='Silk Saree').first()
            
            cart_item1 = Cart(user_id=user.id, product_id=product1.id, quantity=2)
            cart_item2 = Cart(user_id=user.id, product_id=product2.id, quantity=1)
            db.session.add(cart_item1)
            db.session.add(cart_item2)
            db.session.commit()
            
            expected_total = (product1.price * 2) + product2.price
        
        response = self.client.get('/cart')
        self.assertIn(str(expected_total).encode(), response.data)


class TestOrderFunctionality(BaseTestCase):
    """Test order placement and management"""
    
    def test_checkout_requires_login(self):
        """Test checkout requires authentication"""
        response = self.client.get('/checkout', follow_redirects=True)
        self.assertIn(b'Login', response.data)
    
    def test_checkout_page_loads(self):
        """Test checkout page loads for logged-in user"""
        self.login()
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=1)
            db.session.add(cart_item)
            db.session.commit()
        
        response = self.client.get('/checkout')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Checkout', response.data)
    
    def test_place_order_success(self):
        """Test successful order placement"""
        self.login()
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            initial_stock = product.stock
            
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=2)
            db.session.add(cart_item)
            db.session.commit()
        
        response = self.client.post('/place_order', 
                                   data=dict(
                                       shipping_address='123 Test Street, Mumbai',
                                       payment_method='COD'
                                   ),
                                   follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Order placed successfully', response.data)
        
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            order = Order.query.filter_by(user_id=user.id).first()
            self.assertIsNotNone(order)
            self.assertEqual(order.status, 'Pending')
            
            # Check stock was reduced
            product = Product.query.first()
            self.assertEqual(product.stock, initial_stock - 2)
            
            # Check cart was cleared
            cart_items = Cart.query.filter_by(user_id=user.id).all()
            self.assertEqual(len(cart_items), 0)
    
    def test_place_order_insufficient_stock(self):
        """Test order fails with insufficient stock"""
        self.login()
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            product.stock = 1  # Set low stock
            
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=10)
            db.session.add(cart_item)
            db.session.commit()
        
        response = self.client.post('/place_order', 
                                   data=dict(
                                       shipping_address='123 Test Street',
                                       payment_method='COD'
                                   ),
                                   follow_redirects=True)
        
        self.assertIn(b'Insufficient stock', response.data)
    
    def test_view_my_orders(self):
        """Test viewing user's order history"""
        self.login()
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            
            order = Order(user_id=user.id, total_amount=799.00, status='Delivered')
            db.session.add(order)
            db.session.commit()
            
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=1,
                price=product.price
            )
            db.session.add(order_item)
            db.session.commit()
        
        response = self.client.get('/my_orders')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Delivered', response.data)


class TestEdgeCases(BaseTestCase):
    """Test edge cases and error handling"""
    
    def test_invalid_product_id(self):
        """Test accessing non-existent product"""
        response = self.client.get('/product/99999')
        self.assertEqual(response.status_code, 404)
    
    def test_add_zero_quantity_to_cart(self):
        """Test adding zero quantity to cart"""
        self.login()
        with app.app_context():
            product = Product.query.first()
            response = self.client.post(f'/add_to_cart/{product.id}', 
                                       data=dict(quantity=0),
                                       follow_redirects=True)
            
            user = User.query.filter_by(username='testuser').first()
            cart_item = Cart.query.filter_by(user_id=user.id).first()
            # Should either reject or not create cart item
            if cart_item:
                self.assertGreater(cart_item.quantity, 0)
    
    def test_negative_quantity_handling(self):
        """Test handling of negative quantities"""
        self.login()
        with app.app_context():
            product = Product.query.first()
            response = self.client.post(f'/add_to_cart/{product.id}', 
                                       data=dict(quantity=-5),
                                       follow_redirects=True)
            
            # Should not create cart item with negative quantity
            user = User.query.filter_by(username='testuser').first()
            cart_item = Cart.query.filter_by(user_id=user.id).first()
            if cart_item:
                self.assertGreaterEqual(cart_item.quantity, 0)
    
    def test_empty_search_query(self):
        """Test search with empty query"""
        response = self.client.get('/search?q=')
        self.assertEqual(response.status_code, 200)
    
    def test_special_characters_in_search(self):
        """Test search with special characters"""
        response = self.client.get('/search?q=<script>alert("test")</script>')
        self.assertEqual(response.status_code, 200)
        # Should not execute script
        self.assertNotIn(b'<script>', response.data)


class TestDatabaseIntegrity(BaseTestCase):
    """Test database constraints and relationships"""
    
    def test_cascade_delete_user_cart(self):
        """Test deleting user cascades to cart items"""
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            product = Product.query.first()
            
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=1)
            db.session.add(cart_item)
            db.session.commit()
            
            user_id = user.id
            db.session.delete(user)
            db.session.commit()
            
            # Cart items should be deleted
            orphaned_items = Cart.query.filter_by(user_id=user_id).all()
            self.assertEqual(len(orphaned_items), 0)
    
    def test_product_relationships(self):
        """Test product has proper relationships"""
        with app.app_context():
            product = Product.query.first()
            user = User.query.filter_by(username='testuser').first()
            
            # Add to cart
            cart_item = Cart(user_id=user.id, product_id=product.id, quantity=1)
            db.session.add(cart_item)
            
            # Create order
            order = Order(user_id=user.id, total_amount=product.price, status='Pending')
            db.session.add(order)
            db.session.commit()
            
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=1,
                price=product.price
            )
            db.session.add(order_item)
            db.session.commit()
            
            # Product should have relationships
            self.assertGreater(len(Cart.query.filter_by(product_id=product.id).all()), 0)
            self.assertGreater(len(OrderItem.query.filter_by(product_id=product.id).all()), 0)


def run_tests():
    """Run all tests and generate summary"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestModels))
    suite.addTests(loader.loadTestsFromTestCase(TestAuthentication))
    suite.addTests(loader.loadTestsFromTestCase(TestProductRoutes))
    suite.addTests(loader.loadTestsFromTestCase(TestCartFunctionality))
    suite.addTests(loader.loadTestsFromTestCase(TestOrderFunctionality))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestDatabaseIntegrity))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    print("="*70)
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED")
        
        if result.failures:
            print("\nFailed Tests:")
            for test, traceback in result.failures:
                print(f"  - {test}")
        
        if result.errors:
            print("\nTests with Errors:")
            for test, traceback in result.errors:
                print(f"  - {test}")
    
    print("="*70)
    
    return result


if __name__ == '__main__':
    result = run_tests()
    
    # Exit with appropriate code
    exit(0 if result.wasSuccessful() else 1)

"""
Seed data for Indian Clothing Store
Realistic products based on age groups for Indian market
"""

from app import app, db, Category, Product
from datetime import datetime

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Categories based on age groups
        categories_data = [
            {
                'name': 'Infant & Toddler (0-3 years)',
                'age_group': '0-3 years',
                'description': 'Comfortable and soft clothing for babies and toddlers'
            },
            {
                'name': 'Kids Wear (4-12 years)',
                'age_group': '4-12 years',
                'description': 'Playful and durable clothes for growing children'
            },
            {
                'name': 'Teenage Wear (13-19 years)',
                'age_group': '13-19 years',
                'description': 'Trendy and stylish outfits for teenagers'
            },
            {
                'name': 'Young Adults (20-35 years)',
                'age_group': '20-35 years',
                'description': 'Modern fashion for young professionals and students'
            },
            {
                'name': 'Adults (36-55 years)',
                'age_group': '36-55 years',
                'description': 'Elegant and comfortable wear for mature adults'
            },
            {
                'name': 'Senior Wear (56+ years)',
                'age_group': '56+ years',
                'description': 'Comfortable and easy-to-wear clothing for seniors'
            },
            {
                'name': 'Ethnic Wear - All Ages',
                'age_group': 'All Ages',
                'description': 'Traditional Indian clothing for all age groups'
            },
            {
                'name': 'Western Wear - All Ages',
                'age_group': 'All Ages',
                'description': 'Western style clothing for all age groups'
            }
        ]
        
        categories = []
        for cat_data in categories_data:
            category = Category(**cat_data)
            db.session.add(category)
            categories.append(category)
        
        db.session.commit()
        
        # Products - Infant & Toddler (0-3 years)
        infant_products = [
            {
                'name': 'Baby Cotton Romper Set',
                'description': 'Soft cotton romper set for newborns. 100% cotton, breathable fabric. Pack of 3.',
                'price': 599,
                'original_price': 899,
                'category_id': 1,
                'stock': 50,
                'size': '0-6 months, 6-12 months, 12-18 months',
                'color': 'Multi-color (Pastel)',
                'material': '100% Cotton',
                'brand': 'LittleJoys',
                'image_url': '/static/images/baby_romper.jpg',
                'is_featured': True,
                'rating': 4.5
            },
            {
                'name': 'Infant Onesie with Cap',
                'description': 'Adorable onesie with matching cap. Soft and comfortable for baby skin.',
                'price': 399,
                'original_price': 599,
                'category_id': 1,
                'stock': 75,
                'size': '0-3 months, 3-6 months',
                'color': 'Pink, Blue, Yellow',
                'material': 'Cotton Blend',
                'brand': 'BabyLove',
                'image_url': '/static/images/onesie.jpg',
                'is_featured': True,
                'rating': 4.7
            },
            {
                'name': 'Toddler Cotton Frock',
                'description': 'Beautiful printed frock for baby girls. Easy to wear with snap buttons.',
                'price': 449,
                'original_price': 699,
                'category_id': 1,
                'stock': 40,
                'size': '12-18 months, 18-24 months, 2-3 years',
                'color': 'Floral Print',
                'material': 'Cotton',
                'brand': 'TinyTrends',
                'image_url': '/static/images/toddler_frock.jpg',
                'is_featured': False,
                'rating': 4.3
            },
        ]
        
        # Kids Wear (4-12 years)
        kids_products = [
            {
                'name': 'Kids Cotton T-Shirt with Shorts',
                'description': 'Comfortable combo set for active kids. Breathable fabric perfect for Indian climate.',
                'price': 699,
                'original_price': 999,
                'category_id': 2,
                'stock': 100,
                'size': '4-5 years, 6-7 years, 8-9 years, 10-12 years',
                'color': 'Red, Blue, Green, Yellow',
                'material': 'Cotton',
                'brand': 'PlayKids',
                'image_url': '/static/images/kids_tshirt_shorts.jpg',
                'is_featured': True,
                'rating': 4.6
            },
            {
                'name': 'Girls Palazzo with Kurti Set',
                'description': 'Traditional yet comfortable palazzo kurti set for girls. Perfect for casual and festive wear.',
                'price': 899,
                'original_price': 1299,
                'category_id': 2,
                'stock': 60,
                'size': '6-7 years, 8-9 years, 10-12 years',
                'color': 'Pink, Purple, Sky Blue',
                'material': 'Cotton Rayon',
                'brand': 'ChotiPrincess',
                'image_url': '/static/images/girls_palazzo_kurti.jpg',
                'is_featured': True,
                'rating': 4.8
            },
            {
                'name': 'Boys Denim Jeans',
                'description': 'Stretchable denim jeans for boys. Durable and stylish for everyday wear.',
                'price': 799,
                'original_price': 1199,
                'category_id': 2,
                'stock': 80,
                'size': '6-7 years, 8-9 years, 10-12 years',
                'color': 'Blue, Black',
                'material': 'Denim',
                'brand': 'KidsStyle',
                'image_url': '/static/images/boys_jeans.jpg',
                'is_featured': False,
                'rating': 4.4
            },
        ]
        
        # Teenage Wear (13-19 years)
        teen_products = [
            {
                'name': 'Teen Girls Crop Top with Jeans',
                'description': 'Trendy crop top with high-waist jeans combo. Perfect for college and casual outings.',
                'price': 1299,
                'original_price': 1899,
                'category_id': 3,
                'stock': 70,
                'size': 'S, M, L, XL',
                'color': 'Black, White, Denim Blue',
                'material': 'Cotton Lycra',
                'brand': 'TeenFab',
                'image_url': '/static/images/teen_crop_jeans.jpg',
                'is_featured': True,
                'rating': 4.7
            },
            {
                'name': 'Boys Hoodie with Track Pants',
                'description': 'Stylish hoodie and track pants set. Comfortable for sports and casual wear.',
                'price': 1499,
                'original_price': 2199,
                'category_id': 3,
                'stock': 90,
                'size': 'S, M, L, XL',
                'color': 'Black, Grey, Navy Blue',
                'material': 'Cotton Fleece',
                'brand': 'SportyTeens',
                'image_url': '/static/images/boys_hoodie_track.jpg',
                'is_featured': True,
                'rating': 4.5
            },
            {
                'name': 'Teen Girls Kurti with Leggings',
                'description': 'Indo-western kurti with matching leggings. Perfect for college and casual events.',
                'price': 999,
                'original_price': 1499,
                'category_id': 3,
                'stock': 65,
                'size': 'S, M, L, XL',
                'color': 'Floral, Solid colors',
                'material': 'Rayon',
                'brand': 'CollegeDiva',
                'image_url': '/static/images/teen_kurti_legging.jpg',
                'is_featured': False,
                'rating': 4.6
            },
        ]
        
        # Young Adults (20-35 years)
        young_adult_products = [
            {
                'name': 'Men\'s Formal Shirt',
                'description': 'Premium quality formal shirt for office and business meetings. Wrinkle-free fabric.',
                'price': 1299,
                'original_price': 1999,
                'category_id': 4,
                'stock': 120,
                'size': 'S, M, L, XL, XXL',
                'color': 'White, Light Blue, Pink, Grey',
                'material': 'Cotton Polyester',
                'brand': 'OfficeElite',
                'image_url': '/static/images/mens_formal_shirt.jpg',
                'is_featured': True,
                'rating': 4.8
            },
            {
                'name': 'Women\'s Designer Saree',
                'description': 'Elegant designer saree with blouse piece. Perfect for weddings and special occasions.',
                'price': 2499,
                'original_price': 3999,
                'category_id': 4,
                'stock': 50,
                'size': 'Free Size (5.5m)',
                'color': 'Red, Blue, Green, Pink',
                'material': 'Silk Blend',
                'brand': 'SareeKing',
                'image_url': '/static/images/designer_saree.jpg',
                'is_featured': True,
                'rating': 4.9
            },
            {
                'name': 'Men\'s Casual Chinos',
                'description': 'Comfortable chino pants for casual and semi-formal occasions.',
                'price': 1199,
                'original_price': 1799,
                'category_id': 4,
                'stock': 95,
                'size': '30, 32, 34, 36, 38',
                'color': 'Khaki, Navy, Black, Olive',
                'material': 'Cotton Twill',
                'brand': 'UrbanGents',
                'image_url': '/static/images/mens_chinos.jpg',
                'is_featured': False,
                'rating': 4.5
            },
            {
                'name': 'Women\'s Palazzo Suit Set',
                'description': 'Trendy palazzo suit set with dupatta. Comfortable for daily wear and parties.',
                'price': 1799,
                'original_price': 2699,
                'category_id': 4,
                'stock': 70,
                'size': 'S, M, L, XL, XXL',
                'color': 'Pastel shades, Bold prints',
                'material': 'Rayon',
                'brand': 'ChicLadies',
                'image_url': '/static/images/palazzo_suit.jpg',
                'is_featured': True,
                'rating': 4.7
            },
        ]
        
        # Adults (36-55 years)
        adult_products = [
            {
                'name': 'Men\'s Cotton Kurta Pajama',
                'description': 'Traditional cotton kurta pajama set. Perfect for comfort and ethnic occasions.',
                'price': 1499,
                'original_price': 2299,
                'category_id': 5,
                'stock': 85,
                'size': 'M, L, XL, XXL, XXXL',
                'color': 'White, Cream, Light Blue',
                'material': 'Pure Cotton',
                'brand': 'EthnicMan',
                'image_url': '/static/images/kurta_pajama.jpg',
                'is_featured': True,
                'rating': 4.6
            },
            {
                'name': 'Women\'s Cotton Salwar Kameez',
                'description': 'Comfortable cotton salwar kameez with dupatta. Ideal for daily wear and office.',
                'price': 1399,
                'original_price': 2099,
                'category_id': 5,
                'stock': 95,
                'size': 'M, L, XL, XXL, XXXL',
                'color': 'Floral, Printed, Solid',
                'material': 'Cotton',
                'brand': 'ComfortWomen',
                'image_url': '/static/images/salwar_kameez.jpg',
                'is_featured': True,
                'rating': 4.7
            },
            {
                'name': 'Men\'s Formal Trousers',
                'description': 'Premium formal trousers with wrinkle-free fabric. Perfect fit and comfort.',
                'price': 1099,
                'original_price': 1699,
                'category_id': 5,
                'stock': 110,
                'size': '32, 34, 36, 38, 40, 42',
                'color': 'Black, Grey, Navy Blue',
                'material': 'Polyester Viscose',
                'brand': 'CorporateFit',
                'image_url': '/static/images/formal_trousers.jpg',
                'is_featured': False,
                'rating': 4.5
            },
        ]
        
        # Senior Wear (56+ years)
        senior_products = [
            {
                'name': 'Senior Men\'s Comfort Kurta',
                'description': 'Loose-fit comfortable kurta with easy button closure. Breathable cotton fabric.',
                'price': 899,
                'original_price': 1399,
                'category_id': 6,
                'stock': 60,
                'size': 'L, XL, XXL, XXXL',
                'color': 'White, Cream, Light colors',
                'material': 'Pure Cotton',
                'brand': 'SeniorComfort',
                'image_url': '/static/images/senior_kurta.jpg',
                'is_featured': True,
                'rating': 4.8
            },
            {
                'name': 'Senior Women\'s Cotton Nighty',
                'description': 'Comfortable and easy-to-wear cotton nighty. Perfect for home wear and sleep.',
                'price': 599,
                'original_price': 899,
                'category_id': 6,
                'stock': 80,
                'size': 'L, XL, XXL, XXXL',
                'color': 'Pastel prints',
                'material': 'Soft Cotton',
                'brand': 'ComfySeniors',
                'image_url': '/static/images/senior_nighty.jpg',
                'is_featured': True,
                'rating': 4.7
            },
            {
                'name': 'Senior Men\'s Elastic Waist Pants',
                'description': 'Comfortable pants with elastic waist. Easy to wear and maintain.',
                'price': 799,
                'original_price': 1199,
                'category_id': 6,
                'stock': 70,
                'size': 'L, XL, XXL, XXXL',
                'color': 'Grey, Black, Navy',
                'material': 'Cotton Polyester',
                'brand': 'EasyWear',
                'image_url': '/static/images/senior_pants.jpg',
                'is_featured': False,
                'rating': 4.6
            },
        ]
        
        # Ethnic Wear
        ethnic_products = [
            {
                'name': 'Banarasi Silk Saree',
                'description': 'Pure Banarasi silk saree with intricate zari work. Perfect for weddings.',
                'price': 4999,
                'original_price': 7999,
                'category_id': 7,
                'stock': 30,
                'size': 'Free Size (6.3m with blouse)',
                'color': 'Red, Maroon, Royal Blue, Golden',
                'material': 'Pure Silk',
                'brand': 'BanarasiHeritage',
                'image_url': '/static/images/banarasi_saree.jpg',
                'is_featured': True,
                'rating': 4.9
            },
            {
                'name': 'Men\'s Sherwani Set',
                'description': 'Designer sherwani with churidar and dupatta. Perfect for weddings and special events.',
                'price': 5999,
                'original_price': 9999,
                'category_id': 7,
                'stock': 25,
                'size': 'M, L, XL, XXL',
                'color': 'Cream, Golden, Maroon',
                'material': 'Silk Blend',
                'brand': 'RoyalGroom',
                'image_url': '/static/images/sherwani.jpg',
                'is_featured': True,
                'rating': 4.8
            },
            {
                'name': 'Anarkali Suit Set',
                'description': 'Beautiful Anarkali suit with heavy embroidery work. Includes dupatta.',
                'price': 2999,
                'original_price': 4999,
                'category_id': 7,
                'stock': 45,
                'size': 'S, M, L, XL, XXL',
                'color': 'Pink, Red, Green, Blue',
                'material': 'Georgette',
                'brand': 'EthnicDiva',
                'image_url': '/static/images/anarkali.jpg',
                'is_featured': True,
                'rating': 4.7
            },
        ]
        
        # Western Wear
        western_products = [
            {
                'name': 'Women\'s Western Dress',
                'description': 'Stylish western dress for parties and evening events. Modern fit.',
                'price': 1999,
                'original_price': 2999,
                'category_id': 8,
                'stock': 55,
                'size': 'S, M, L, XL',
                'color': 'Black, Red, Navy',
                'material': 'Polyester Crepe',
                'brand': 'PartyGlam',
                'image_url': '/static/images/western_dress.jpg',
                'is_featured': True,
                'rating': 4.6
            },
            {
                'name': 'Men\'s Denim Jacket',
                'description': 'Classic denim jacket for casual style. Perfect for all seasons.',
                'price': 2499,
                'original_price': 3999,
                'category_id': 8,
                'stock': 40,
                'size': 'M, L, XL, XXL',
                'color': 'Light Blue, Dark Blue, Black',
                'material': 'Denim',
                'brand': 'CasualKing',
                'image_url': '/static/images/denim_jacket.jpg',
                'is_featured': True,
                'rating': 4.7
            },
        ]
        
        # Add all products to database
        all_products = (
            infant_products + kids_products + teen_products +
            young_adult_products + adult_products + senior_products +
            ethnic_products + western_products
        )
        
        for product_data in all_products:
            product = Product(**product_data)
            db.session.add(product)
        
        db.session.commit()
        print(f"✅ Database seeded successfully!")
        print(f"✅ Created {len(categories)} categories")
        print(f"✅ Created {len(all_products)} products")

if __name__ == '__main__':
    seed_database()

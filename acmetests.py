import unittest
import random
from acme import Product
from acme_report import generate_products, naming_adjectives, naming_nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_range_stealability(self):
        test_price = random.randrange(0,100)
        test_weight_high = test_price / 3
        test_weight_low = test_price * 3

        prod_high = Product(name='Test Product', price=test_price, weight=test_weight_high)
        prod_low = Product(name='Test Product', price=test_price, weight=test_weight_low)

        self.assertEqual(prod_high.stealability(), "Very stealable!")
        self.assertEqual(prod_low.stealability(), "Kinda stealable.")

    def test_range_explode(self):
        test_flammability = random.uniform(1,2.5)
        test_weight_high = 1000
        test_weight_medium = 10
        test_weight_low = test_flammability

        prod_high = Product('test_high', flammability=test_flammability, weight=test_weight_high)
        prod_medium = Product('test_high', flammability=test_flammability, weight=test_weight_medium)
        prod_low = Product('test_high', flammability=test_flammability, weight=test_weight_low)

        self.assertEqual(prod_high.explode(), "...BABOOM!!",)
        self.assertEqual(prod_medium.explode(), "...boom!")
        self.assertEqual(prod_low.explode(), "...fizzle.")


class AcmeReportTests(unittest.TestCase):

    def setUp(self):
        self.num_products = 30
        self.products = generate_products(num_products=self.num_products)

    def test_num_products(self):
        self.assertEqual(len(self.products), self.num_products)

    def test_legal_names(self):
        for product in self.products:
            adjective = product.name.split(' ')[0]
            noun = product.name.split(' ')[1]
            self.assertIn(adjective, naming_adjectives)
            self.assertIn(noun, naming_nouns)

if __name__ == '__main__':
    unittest.main()
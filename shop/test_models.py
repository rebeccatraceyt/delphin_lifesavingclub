from django.test import TestCase
from .models import (
    ProductOption,
    Category,
    Product,
)

# ------ Product Categories ------


class TestCategoryModel(TestCase):
    """Test Category Model"""

    def test_category_model(self):
        # Create Test Category
        category = Category(name='Test Category')

        # Save Test Category
        category.save()

        # check that Field == Value
        self.assertEqual(category.name, "Test Category")

    def test_category_as_string(self):
        category = Category(name='test')
        category.save()
        self.assertEqual('test', str(category))


# ------ Product Filters ------


class TestProductOptionModel(TestCase):
    """Test Product Options Model"""

    def test_product_option_model(self):
        # Create Test ProductOption
        product_option = ProductOption(product_option='Test Product Option')

        # Save Test Option
        product_option.save()

        # check that Field == Value
        self.assertEqual(product_option.product_option, "Test Product Option")

    def test_product_option_as_string(self):
        product_option = ProductOption(product_option='test')
        product_option.save()
        self.assertEqual('test', str(product_option))


# ------ All Products ------


class TestProductModel(TestCase):
    """Test Product Model"""

    def test_product_model(self):
        # Create Test Category
        category = Category.objects.create(name='Test Category')

        # Create Test Option
        product_option = ProductOption(product_option='Test Product Option')

        # Create Test Product
        product = Product(name='test product',
                          description='test description',
                          price='90.00',
                          image='img.jpg',)

        # Save Test Product
        product.category_id = category.id
        product.product_option_id = product_option.id
        product.save()

        # check that Field == Value
        self.assertEqual(product.name, "test product")
        self.assertEqual(product.description, "test description")
        self.assertEqual(product.price, "90.00")
        self.assertEqual(product.image, "img.jpg")
        self.assertEqual(product.category_id, category.id)
        self.assertEqual(product.product_option_id, product_option.id)

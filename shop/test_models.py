from django.test import TestCase
from .models import (
    Time,
    Size,
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


# ------ Course Filters ------


class TestTimeModel(TestCase):
    """Test Time Model"""

    def test_time_model(self):
        # Create Test Time
        time = Time(time='Test Time')

        # Save Test Time
        time.save()

        # check that Field == Value
        self.assertEqual(time.time, "Test Time")

    def test_time_as_string(self):
        time = Time(time='test')
        time.save()
        self.assertEqual('test', str(time))


# ------ Apparel Filters ------


class TestSizeModel(TestCase):
    """Test Size Model"""

    def test_size_model(self):
        # Create Test Size
        size = Size(size='Test Size')

        # Save Test Size
        size.save()

        # check that Field == Value
        self.assertEqual(size.size, "Test Size")

    def test_size_as_string(self):
        size = Size(size='test')
        size.save()
        self.assertEqual('test', str(size))


# ------ All Products ------


class TestProductModel(TestCase):
    """Test Product Model"""

    def test_course_model(self):
        # Create Test Category
        category = Category.objects.create(name='Test Category')

        # Create Test Time
        time = Time.objects.create(time='Test Time')

        # Create Test Product
        product = Product(name='test product',
                          description='test description',
                          price='90.00',
                          image='img.jpg',)

        # Save Test Product
        product.category_id = category.id
        product.time_id = time.id
        product.save()

        # check that Field == Value
        self.assertEqual(product.name, "test product")
        self.assertEqual(product.description, "test description")
        self.assertEqual(product.price, "90.00")
        self.assertEqual(product.image, "img.jpg")
        self.assertEqual(product.category_id, 1)
        self.assertEqual(product.time_id, 1)

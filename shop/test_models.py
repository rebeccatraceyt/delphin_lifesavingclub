from django.test import TestCase
from .models import (
    Time,
    Size,
    Category,
    Product,
    CourseTime,
    ApparelSize
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


# ------ ManyToMany Through Tables ------


class TestCourseTimeModel(TestCase):
    """Test Course Time Model"""

    def test_course_time_model(self):

        # Create Test Time
        time = Time.objects.create(time='Test Time')

        # Create Test Course
        product = Product(name='test course',
                          description='test description',
                          price='90.00',
                          image='img.jpg',)

        # Create Test Stock Count
        course_time = CourseTime(stock_count=3)

        # Save Test Course Time
        course_time.time_id = time.id
        course_time.product_id = product.id
        course_time.save()

        self.assertEqual(course_time.time_id, 1)
        self.assertEqual(course_time.product.name, "test course")
        self.assertEqual(course_time.stock_count, 3)


class TestApparelSizeModel(TestCase):
    """Test Apparel Size Model"""

    def test_apparel_size_model(self):

        # Create Test Size
        size = Size.objects.create(size='Test Size')

        # Create Test Course
        product = Product.objects.create(name='test apparel',
                                         description='test description',
                                         price='90.00',
                                         image='img.jpg',)

        # Create Test Stock Count
        apparel_size = ApparelSize(stock_count=3)

        # Save Test Apparel Size
        apparel_size.size_id = size.id
        apparel_size.product_id = product.id
        apparel_size.save()

        self.assertEqual(apparel_size.size_id, 1)
        self.assertEqual(apparel_size.product.name, "test apparel")
        self.assertEqual(apparel_size.stock_count, 3)

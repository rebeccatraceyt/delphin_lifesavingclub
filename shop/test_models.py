from django.test import TestCase
from .models import (
    ProductType,
    Time,
    AgeRange,
    Course,
    CourseTime,
    Size,
    Category,
    Apparel,
    ApparelSize
)

# ------ Product Types ------


class TestProductTypeModel(TestCase):
    """Test Product Type Model"""

    def test_product_type_model(self):
        # Create Test ProductType
        product_type = ProductType(name='Test Product Type')

        # Save Test ProductType
        product_type.save()

        # check that Field == Value
        self.assertEqual(product_type.name, "Test Product Type")

    def test_product_type_as_string(self):
        product_type = ProductType(name='test')
        product_type.save()
        self.assertEqual('test', str(product_type))


# ------ Courses ------


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


class TestAgeRangeModel(TestCase):
    """Test AgeRange Model"""

    def test_age_range_model(self):
        # Create Test AgeRange
        age_range = AgeRange(name='Test AgeRange')

        # Save Test AgeRange
        age_range.save()

        # check that Field == Value
        self.assertEqual(age_range.name, "Test AgeRange")

    def test_age_range_as_string(self):
        age_range = AgeRange(name='test')
        age_range.save()
        self.assertEqual('test', str(age_range))


class TestCourseModel(TestCase):
    """Test Course Model"""

    def test_course_model(self):
        # Create Test Product Type
        product_type = ProductType.objects.create(name='Test Product Type')

        # Create Test Age Range
        age_range = AgeRange.objects.create(name='Test Age Range')

        # Create Test Time
        time = Time.objects.create(time='Test Time')

        # Create Test Course
        course = Course(name='test course',
                        description='test description',
                        price='90.00',
                        lvl_age='3',
                        image='img.jpg',)

        # Save Test Course
        course.product_type_id = product_type.id
        course.age_range_id = age_range.id
        course.time_id = time.id
        course.save()

        # check that Field == Value
        self.assertEqual(course.name, "test course")
        self.assertEqual(course.description, "test description")
        self.assertEqual(course.price, "90.00")
        self.assertEqual(course.lvl_age, "3")
        self.assertEqual(course.image, "img.jpg")
        self.assertEqual(course.product_type_id, 1)
        self.assertEqual(course.age_range_id, 1)
        self.assertEqual(course.time_id, 1)


class TestCourseTimeModel(TestCase):
    """Test Course Time Model"""

    def test_course_time_model(self):

        # Create Test Time
        time = Time.objects.create(time='Test Time')

        # Create Test Course
        course = Course.objects.create(name='test course',
                                       description='test description',
                                       price='90.00',
                                       lvl_age='3',
                                       image='img.jpg',)

        # Create Test Stock Count
        course_time = CourseTime(stock_count=3)

        # Save Test Course Time
        course_time.time_id = time.id
        course_time.course_id = course.id
        course_time.save()

        self.assertEqual(course_time.time_id, 1)
        self.assertEqual(course_time.course.name, "test course")
        self.assertEqual(course_time.stock_count, 3)


# ------ Apparel ------


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


class TestApparelModel(TestCase):
    """Test Apparel Model"""

    def test_apparel_model(self):
        # Create Test Product Type
        product_type = ProductType.objects.create(name='Test Product Type')

        # Create Test Age Range
        category = Category.objects.create(name='Test Category')

        # Create Test Size
        size = Size.objects.create(size='Test Size')

        # Create Test Apparel
        apparel = Apparel(name='test apparel',
                          description='test description',
                          price='90.00',
                          image='img.jpg',)

        # Save Test Apparel
        apparel.product_type_id = product_type.id
        apparel.category_id = category.id
        apparel.size_id = size.id
        apparel.save()

        # check that Field == Value
        self.assertEqual(apparel.name, "test apparel")
        self.assertEqual(apparel.description, "test description")
        self.assertEqual(apparel.price, "90.00")
        self.assertEqual(apparel.image, "img.jpg")
        self.assertEqual(apparel.product_type_id, 1)
        self.assertEqual(apparel.category_id, 1)
        self.assertEqual(apparel.size_id, 1)


class TestApparelSizeModel(TestCase):
    """Test Apparel Size Model"""

    def test_apparel_size_model(self):

        # Create Test Size
        size = Size.objects.create(size='Test Size')

        # Create Test Course
        apparel = Apparel.objects.create(name='test apparel',
                                         description='test description',
                                         price='90.00',
                                         image='img.jpg',)

        # Create Test Stock Count
        apparel_size = ApparelSize(stock_count=3)

        # Save Test Apparel Size
        apparel_size.size_id = size.id
        apparel_size.apparel_id = apparel.id
        apparel_size.save()

        self.assertEqual(apparel_size.size_id, 1)
        self.assertEqual(apparel_size.apparel.name, "test apparel")
        self.assertEqual(apparel_size.stock_count, 3)

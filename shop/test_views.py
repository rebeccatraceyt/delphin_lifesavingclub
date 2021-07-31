from django.test import TestCase
from django.urls import reverse
from .models import Course, Apparel, Category, AgeRange


# ------ All Products ------


class TestAllProductsView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('all_products'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('all_products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/shop_products.html')


class TestSearchProductsView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/search_shop.html')


# ------ Courses ------


class TestAllCoursesView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/shop/all_courses')
        self.assertEqual(response.status_code, 200)

    def test_view_sort_by_age_range(self):
        """ Test sorting functionality """
        age_range = AgeRange.objects.create(name='test range')
        course = Course.objects.create(name='test course',
                                       price='22',
                                       image='test.png',
                                       description='test desc',
                                       )
        course.age_range = age_range
        course.save()

        response = self.client.get(
            '/shop/all_courses?age_range={age_range}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/all_courses.html')

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('all_courses'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('all_courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/all_courses.html')


class TestCourseDetailView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        course = Course.objects.create(name='test course',
                                       price='22',
                                       image='test.png',
                                       description='test desc',
                                       )
        response = self.client.get(
            '/shop/course/{0}'.format(course.id))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        course = Course.objects.create(name='test course',
                                       price='22',
                                       image='test.png',
                                       description='test desc',
                                       pk='4',
                                       )
        response = self.client.get(
            '/shop/course/{0}'.format(course.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/course_detail.html')


# ------ Apparel ------


class TestAllApparelView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/shop/all_apparel')
        self.assertEqual(response.status_code, 200)

    def test_view_sort_by_category(self):
        """ Test sorting functionalirt """
        category = Category.objects.create(name='test category')
        apparel = Apparel.objects.create(name='test apparel',
                                         price='22',
                                         image='test.png',
                                         description='test desc',
                                         )
        apparel.category = category
        apparel.save()

        response = self.client.get(
            '/shop/all_apparel?category={category}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/all_apparel.html')

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('all_apparel'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('all_apparel'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/all_apparel.html')


class TestApparelDetailView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        apparel = Apparel.objects.create(name='test apparel',
                                         price='22',
                                         image='test.png',
                                         description='test desc',
                                         )
        response = self.client.get(
            '/shop/apparel/{0}'.format(apparel.id))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        apparel = Apparel.objects.create(name='test apparel',
                                         price='22',
                                         image='test.png',
                                         description='test desc',
                                         pk='4',
                                         )
        response = self.client.get(
            '/shop/apparel/{0}'.format(apparel.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/apparel_detail.html')

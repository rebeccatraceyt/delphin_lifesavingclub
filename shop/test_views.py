from django.test import TestCase
from django.urls import reverse
from .models import Course, Apparel


class TestAllProductsView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('all_products'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('all_products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/shop_products.html')


class TestAllCoursesView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/shop/all_courses')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('all_courses'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('all_courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/all_courses.html')


class TestCourseDetailView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        course = Course.objects.create(name='test course',
                                       price='22',
                                       image='test.png',
                                       description='test desc',
                                       )
        response = self.client.get(
            '/shop/course/{0}'.format(course.id))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
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


class TestAllApparelView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/shop/all_apparel')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('all_apparel'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('all_apparel'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/all_apparel.html')


class TestApparelDetailView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        apparel = Apparel.objects.create(name='test apparel',
                                         price='22',
                                         image='test.png',
                                         description='test desc',
                                         )
        response = self.client.get(
            '/shop/apparel/{0}'.format(apparel.id))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
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

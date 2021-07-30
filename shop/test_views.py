from django.test import TestCase
from django.urls import reverse


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

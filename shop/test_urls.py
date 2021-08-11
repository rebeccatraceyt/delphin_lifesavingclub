from django.test import TestCase
from django.urls import reverse, resolve
from .views import (
    all_products,
    search,
    product_detail,
    courses,
    apparel
)


class TestUrls(TestCase):
    """ Tests for urls in cart app """

    def test_all_products_url_is_resolved(self):
        url = reverse('all_products')
        self.assertEqual(resolve(url).func, all_products)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)

    def test_product_detail_url_is_resolved(self):
        url = reverse('product_detail', args=['test-product-id'])
        self.assertEqual(resolve(url).func, product_detail)

    def test_courses_url_is_resolved(self):
        url = reverse('courses')
        self.assertEqual(resolve(url).func, courses)

    def test_apparel_url_is_resolved(self):
        url = reverse('apparel')
        self.assertEqual(resolve(url).func, apparel)

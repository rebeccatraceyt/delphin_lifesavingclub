from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Category


# ------ All Products ------


class TestAllProductsView(TestCase):
    def setUp(self):
        self.client = Client()

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
    def setUp(self):
        self.client = Client()

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


class TestProductDetailView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        product = Product.objects.create(name='test product',
                                         price='22',
                                         image='test.png',
                                         description='test desc',
                                         )
        response = self.client.get(
            '/shop/product/{0}'.format(product.id))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        product = Product.objects.create(name='test product',
                                         price='22',
                                         image='test.png',
                                         description='test desc',
                                         pk='4',
                                         )
        response = self.client.get(
            '/shop/product/{0}'.format(product.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product.html')


# ------ All Courses ------


class TestAllCoursesView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/shop/courses')
        self.assertEqual(response.status_code, 200)

    def test_view_sort_by_category(self):
        """ Test sorting functionality """
        category = Category.objects.create(name='test category')
        course = Product.objects.create(name='test course',
                                        price='22',
                                        image='test.png',
                                        description='test desc',
                                        )
        course.category = category
        course.save()

        response = self.client.get(
            '/shop/courses?category={category}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/courses.html')

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/courses.html')


# ------ All Apparel ------


class TestAllApparelView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/shop/apparel')
        self.assertEqual(response.status_code, 200)

    def test_view_sort_by_category(self):
        """ Test sorting functionality """
        category = Category.objects.create(name='test category')
        apparel = Product.objects.create(name='test apparel',
                                         price='22',
                                         image='test.png',
                                         description='test desc',
                                         )
        apparel.category = category
        apparel.save()

        response = self.client.get(
            '/shop/apparel?category={category}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/apparel.html')

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('apparel'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('apparel'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/apparel.html')

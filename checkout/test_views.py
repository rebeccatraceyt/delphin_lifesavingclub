from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product


class TestCheckoutView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/checkout/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        """ Test correct template redirects to all_products """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/shop/')


class TestOrderDetailsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/checkout/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('order_review'))
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        """ Test correct template redirects to all_products """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/shop/')

    def test_post_valid_order(self):
        """ Test order post """
        # login the user
        self.client.login(username='username',
                          password='password')

        # create an item
        item = Product.objects.create(name='test product',
                                      price='22',
                                      image='test.png',
                                      description='test desc',)

        # add item to cart
        self.client.post("/shopping_bag/add/{0}".format(item.id),
                         data={'quantity': '2'})

        # get the stripe publisable key
        stripe_id = 'tok_visa'

        # send the order
        response = self.client.post("/checkout/", {
            'full_name': 'name',
            'phone_number': '000',
            'email': 'test@test.com',
            'street_address1': 'address 1',
            'street_address2': 'address 2',
            'town_or_city': 'city',
            'county': 'county',
            'country': 'country',
            'postcode': 'code13',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2022',
            'stripe_id': stripe_id},
            follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/shop/')

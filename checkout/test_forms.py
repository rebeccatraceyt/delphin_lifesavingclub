from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    def test_order_form_valid(self):
        form = OrderForm({'full_name': "Test Full Name",
                          'email': "Test Email",
                          'phone_number': "1234567890",
                          'postcode': "Test123",
                          'town_or_city': "Test Town",
                          'street_address1': "Test Street Address1",
                          'street_address2': "Test Street Address2",
                          'county': "Co. Test",
                          })
        self.assertFalse(form.is_valid())

    def test_full_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_postcode_is_not_required(self):
        form = OrderForm({'full_name': 'Test Full Name',
                          'email': 'Test Email',
                          'phone_number': 'Test Phone Number',
                          'street_address1': 'Test Street Address 1',
                          'street_address2': 'Test Street Address 2',
                          'town_or_city': 'Test Town or City'})
        self.assertTrue(form.is_valid)

    def test_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_street_address2_is_not_required(self):
        form = OrderForm({'full_name': 'Test Full Name',
                          'email': 'Test Email',
                          'phone_number': 'Test Phone Number',
                          'street_address1': 'Test Street Address1',
                          })
        self.assertTrue(form.is_valid)

    def test_county_is_not_required(self):
        form = OrderForm({'full_name': 'Test Full Name',
                          'email': 'Test Email',
                          'phone_number': 'Test Phone Number',
                          'street_address1': 'Test Street Address 1',
                          'street_address2': 'Test Street Address 2',
                          'town_or_city': 'Test Town or City',
                          'postcode': 'Test Postcode'})
        self.assertTrue(form.is_valid)

    def test_fields_are_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
                         'full_name', 'email',
                         'phone_number',
                         'street_address1',
                         'street_address2',
                         'town_or_city',
                         'postcode',
                         'country',
                         'county'))

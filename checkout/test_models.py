
from django.test import TestCase
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from shop.models import Product


class TestOrderModel(TestCase):
    '''Test Order Model'''

    def test_order_model(self):
        # create a user
        user = User.objects.create(username='name')

        # Create an order
        order = Order(full_name='name',
                      email='email@email.com',
                      phone_number='0000',
                      town_or_city='city',
                      street_address1='street address 1',
                      street_address2='street address 2',
                      country='country',
                      county='county',
                      postcode='postcode',)

        order.user_id = user.id
        order.save()

        # check to see that the review summary equal the saved review value
        self.assertEqual(order.full_name, "name")
        self.assertEqual(order.email, 'email@email.com')
        self.assertEqual(order.phone_number, '0000')
        self.assertEqual(order.town_or_city, "city")
        self.assertEqual(order.street_address1, 'street address 1')
        self.assertEqual(order.street_address2, 'street address 2')
        self.assertEqual(order.country, "country")
        self.assertEqual(order.county, 'county')
        self.assertEqual(order.postcode, 'postcode')

    def test_order_line_item_model(self):
        ''' Test Order Line Item Model'''

        # create a user
        user = User.objects.create(username='name')

        # create a product
        product = Product.objects.create(name='test product', price=2)

        # Create an order
        order = Order.objects.create(full_name='name',
                                     email='email@email.com',
                                     phone_number='0000',
                                     town_or_city='city',
                                     street_address1='street address 1',
                                     street_address2='street address 2',
                                     country='country',
                                     county='county',
                                     postcode='postcode',
                                     )

        order.user_id = user.id
        order.save()

        orderlineitem = OrderLineItem(quantity=2,
                                      lineitem_total=4,)
        orderlineitem.user_id = user.id
        orderlineitem.product_id = product.id
        orderlineitem.order_id = order.id

        # check to see that the review summary equal the saved review value
        self.assertEqual(orderlineitem.user_id, 1)
        self.assertEqual(orderlineitem.product_id, 1)
        self.assertEqual(orderlineitem.order_id, 1)
        self.assertEqual(orderlineitem.quantity, 2)
        self.assertEqual(orderlineitem.lineitem_total, 4)

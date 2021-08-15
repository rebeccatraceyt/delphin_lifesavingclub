from django.test import TestCase
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from shop.models import Product


class TestOrderModel(TestCase):
    """ Test Order Model """

    def test_order_model(self):
        # create a user
        user = User.objects.create(username='name')

        # get the stripe publisable key
        stripe_id = 'tok_visa'

        # Create an order
        order = Order(delivery_cost=3.00,
                      order_total=24.99,
                      grand_total=27.99,
                      original_bag='test bag',
                      stripe_pid=stripe_id,)

        order.user_id = user.id
        order.save()

        # check to see that the review summary equal the saved review value
        self.assertEqual(order.delivery_cost, 3.00)
        self.assertEqual(order.order_total, 24.99)
        self.assertEqual(order.grand_total, 27.99)
        self.assertEqual(order.original_bag, 'test bag')

    def test_order_line_item_model(self):
        """ Test Order Line Item Model """

        # create a user
        user = User.objects.create(username='name')

        # create a product
        product = Product.objects.create(name='test product', price=24.99)

        # Create an order
        # get the stripe publisable key
        stripe_id = 'tok_visa'

        # Create an order
        order = Order(delivery_cost=3.00,
                      order_total=24.99,
                      grand_total=27.99,
                      original_bag='test bag',
                      stripe_pid=stripe_id,)

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

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from shopping_bag.contexts import bag_content

import stripe


def checkout(request):
    """
    Begins checkout process.
    Directs user to Order Review page.
    """
    current_bag = request.session.get('current_bag', {})
    if not current_bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('all_products'))

    return redirect(reverse('order_review'))


def order_review(request):
    """
    Crispy form allowing user to enter their information.
    Removes navbar and footer from page to follow eCommerce conventions.
    Hide Elements ref: https://tinyurl.com/yp2buee3
    """

    current_bag = request.session.get('current_bag', {})
    if not current_bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('all_products'))

    context = {
        'active_page': 'order_review',
        'navbar': False,
        'footer': False,
    }

    return render(request, 'checkout/order_review.html', context)


def order_details(request):
    """
    Crispy form allowing user to enter their information.
    Removes navbar and footer from page to follow eCommerce conventions.
    Hide Elements ref: https://tinyurl.com/yp2buee3
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_bag = request.session.get('current_bag', {})
    if not current_bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('all_products'))

    order_bag = bag_content(request)
    total = order_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe Public Key is missing, \
            Did you forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'active_page': 'order_details',
        'navbar': False,
        'footer': False,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/order_details.html', context)

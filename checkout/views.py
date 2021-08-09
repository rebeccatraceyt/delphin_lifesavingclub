from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404,
                              HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from shop.models import Product
from shopping_bag.contexts import bag_content

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Determines whether user has save info box checked
    Returns this to the webhook
    """
    try:
        # POST request with client secret and payment intent
        # payment intent id
        pid = request.POST.get('client_secret').split('_secret')[0]

        # stipe keys is used to modify payment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'current_bag': json.dumps(request.session.get('current_bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


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

    if request.method == 'POST':
        current_bag = request.session.get('current_bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'eircode': request.POST['eircode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in current_bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    for select, quantity in item_data['items_by_select'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_select=select,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    # if product is not found
                    messages.error(request, (
                        "One of the products wasn't found in our database."
                        "Contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_bag'))
            # whether user wants to save produle info to session
            request.session['save_info'] = 'save-info' in request.POST

            # redirect to success page
            return redirect(
                reverse('order_complete', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your order form. \
            Please double check your information.')

    else:
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


def order_complete(request, order_number):
    """
    Handle successful checkouts
    """
    # check if user wanted to save info
    save_info = request.session.get('save_info')

    # get order to send to template
    order = get_object_or_404(Order, order_number=order_number)

    # delete session bag
    if 'current_bag' in request.session:
        del request.session['current_bag']

    context = {
        'order': order,
        'active_page': 'order_complete',
    }

    return render(request, 'checkout/order_complete.html', context)

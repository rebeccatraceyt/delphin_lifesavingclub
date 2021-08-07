from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    Begins checkout process.
    Directs user to Order Info page.
    """
    current_bag = request.session.get('current_bag', {})
    if not current_bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('all_products'))

    return redirect(reverse('order_info'))


def order_info(request):
    """
    Crispy form allowing user to enter their information.
    Removes navbar and footer from page to follow eCommerce conventions.
    Hide Elements ref: https://tinyurl.com/yp2buee3
    """

    current_bag = request.session.get('current_bag', {})
    if not current_bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('all_products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'active_page': 'order_info',
        'navbar': False,
        'footer': False,
    }

    return render(request, 'checkout/order_info.html', context)
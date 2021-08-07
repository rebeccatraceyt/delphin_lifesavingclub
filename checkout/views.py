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

    current_bag = request.session.get('current_bag', {})
    if not current_bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('all_products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/order_info.html', context)

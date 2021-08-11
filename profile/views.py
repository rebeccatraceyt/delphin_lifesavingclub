from django.shortcuts import render, get_object_or_404
from django.contrib import messages


from .models import UserProfile
from .forms import ProfileForm
from checkout.models import Order


def profile(request):
    """
    Display user profile
    Adapted from Boutique Ado Mini Project
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    # if user changes information on profile page:
    if request.method == 'POST':
        # create new instance of the user profile form using post data
        form = ProfileForm(request.POST, instance=profile)

        # checks if form is valid
        if form.is_valid():
            # valid = save and send success message
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = ProfileForm(instance=profile)

    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
        'just_message': True,
    }

    return render(request, 'profile/profile.html', context)


def order_history(request, order_number):
    """
    Get Users past order history
    """
    # get past orders
    order = get_object_or_404(Order, order_number=order_number)

    # informative message on previous orders
    messages.info(request, (
        f'This a past order confirmation for order number {order_number}.'
        'A confirmation email was sent on order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/order_complete.html', context)

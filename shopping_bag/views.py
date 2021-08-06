from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from shop.models import Course, Apparel
from queryset_sequence import QuerySetSequence


def view_bag(request):
    """
    Returns Shopping Bag
    """
    return render(request, 'shopping_bag/view_bag.html')


def add_to_bag(request, item_id):
    """
    Submit form to view
        defines quantity of product added to shopping bag
    """

    products = QuerySetSequence(Course.objects.all(),
                                Apparel.objects.all())
    product = get_object_or_404(products, pk=item_id)

    # Get quantity of item and add to current bag
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # get products
    select = None
    if 'product_select' in request.POST:
        select = request.POST['product_select']

    current_bag = request.session.get('current_bag', {})

    # checks if item has size or time
    if item_id in list(current_bag.keys()):
        # if item is currently in bag
        if select in current_bag[item_id]['items_by_select'].keys():
            # if item is same size/time, increment quantity
            current_bag[item_id]['items_by_select'][select] += quantity
            messages.success(
                request,
                f'QTY updated for: {product.name}')
        else:
            # if item is different size/time, add new item
            current_bag[item_id]['items_by_select'][select] = quantity
            messages.success(request, f'Added {product.name} to your bag')
    else:
        # if not currently in bag, add new item
        current_bag[item_id] = {'items_by_select': {select: quantity}}
        messages.success(request, f'Added {product.name} to your bag')

    # override session variable with update
    request.session['current_bag'] = current_bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """
    Submit update form to view to update shopping bag
    """

    products = QuerySetSequence(Course.objects.all(), Apparel.objects.all())
    product = get_object_or_404(products, pk=item_id)

    # Get quantity of item and add to current bag
    quantity = int(request.POST.get('quantity'))

    # get apparel products
    select = None
    if 'product_select' in request.POST:
        select = request.POST['product_select']

    current_bag = request.session.get('current_bag', {})

    if quantity > 0:
        current_bag[item_id]['items_by_select'][select] = quantity
        messages.success(
                request,
                f'QTY updated for: {product.name}')
    else:
        del current_bag[item_id]['items_by_select'][select]
        if not current_bag[item_id]['items_by_select']:
            current_bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    # override session variable with update
    request.session['current_bag'] = current_bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Submit remove form to view to remove item from shopping bag
    """

    try:
        products = QuerySetSequence(Course.objects.all(),
                                    Apparel.objects.all())
        product = get_object_or_404(products, pk=item_id)

        # get apparel products
        select = None
        if 'product_select' in request.POST:
            select = request.POST['product_select']

        current_bag = request.session.get('current_bag', {})

        del current_bag[item_id]['items_by_select'][select]
        if not current_bag[item_id]['items_by_select']:
            current_bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['current_bag'] = current_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

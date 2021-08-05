from django.shortcuts import render, redirect


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

    # Get quantity of item and add to current bag
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # get apparel products
    product_select = None
    if 'apparel_size' in request.POST:
        product_select = request.POST['apparel_size']

    # get course products
    if 'course_time' in request.POST:
        product_select = request.POST['course_time']

    current_bag = request.session.get('current_bag', {})

    # checks if item has size or time
    if product_select:
        if item_id in list(current_bag.keys()):
            # if item is currently in bag
            if product_select in current_bag[item_id]['items_by_select'].keys():
                # if item is same size/time, increment quantity
                current_bag[item_id]['items_by_select'][product_select] += quantity
            else:
                # if item is different size/time, add new item
                current_bag[item_id]['items_by_select'][product_select] = quantity
        else:
            # if not currently in bag, add new item
            current_bag[item_id] = {'items_by_select': {product_select: quantity}}
    else:
        # if apparel item has no size
        # check if item exists already in bag
        if item_id in list(current_bag.keys()):
            # if it does, increment quantity number
            current_bag[item_id] += quantity
        else:
            current_bag[item_id] = quantity

    # override session variable with update
    request.session['current_bag'] = current_bag
    return redirect(redirect_url)

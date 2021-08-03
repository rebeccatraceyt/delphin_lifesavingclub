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
    current_bag = request.session.get('current_bag', {})

    # check if item exists already in bag
    # if it does, increment quantity number
    if item_id in list(current_bag.keys()):
        current_bag[item_id] += quantity
    else:
        current_bag[item_id] = quantity

    # override session variable with update
    request.session['current_bag'] = current_bag
    print(request.session['current_bag'])
    return redirect(redirect_url)

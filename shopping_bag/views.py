from django.shortcuts import render


def view_bag(request):
    """
    Returns Shopping Bag
    """
    return render(request, 'shopping_bag/view_bag.html')

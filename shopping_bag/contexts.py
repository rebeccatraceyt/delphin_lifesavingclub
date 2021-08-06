from django.shortcuts import get_object_or_404
from queryset_sequence import QuerySetSequence
from decimal import Decimal
from django.conf import settings
from shop.models import Course, Apparel


def bag_content(request):
    """
    Context processor allowing bag content dictionary to be
    accessible across app.

    Copied and edited from Boutique Ado mini project
    https://tinyurl.com/5f7ypxcc
    """

    courses = Course.objects.all()
    apparel = Apparel.objects.all()
    products = QuerySetSequence(Course.objects.all(), Apparel.objects.all())

    bag_items = []
    total = 0
    product_count = 0
    current_bag = request.session.get('current_bag', {})

    # for items/quantity in session bag
    for item_id, item_data in current_bag.items():
        product = get_object_or_404(products, pk=item_id)

        for select, quantity in item_data['items_by_select'].items():

            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'product_select': select,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'courses': courses,
        'apparel': apparel,
    }

    return context

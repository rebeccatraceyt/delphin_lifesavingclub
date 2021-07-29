from django.shortcuts import render
from .models import Course, Apparel


def all_products(request):
    """
    Returns All Apparel
    """

    courses = Course.objects.all()
    apparel = Apparel.objects.all()

    context = {
        'apparel': apparel,
        'courses': courses
    }

    return render(request, 'products/products.html', context)

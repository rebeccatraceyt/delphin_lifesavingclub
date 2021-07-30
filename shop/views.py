from django.shortcuts import render, get_object_or_404
from queryset_sequence import QuerySetSequence
from .models import Course, Apparel


# ------ All Products ------


def all_products(request):
    """
    Returns all products
    ref: https://pypi.org/project/django-querysetsequence/
    """
    products = QuerySetSequence(Course.objects.all(), Apparel.objects.all())

    context = {
        'products': products
    }

    return render(request, 'shop/shop_products.html', context)

# ------ Courses ------


def all_courses(request):
    """
    Returns All Courses
    """

    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'shop/all_courses.html', context)


# ------ Apparel ------


def all_apparel(request):
    """
    Returns All Apparel
    """

    apparel = Apparel.objects.all()

    context = {
        'apparel': apparel
    }

    return render(request, 'shop/all_apparel.html', context)


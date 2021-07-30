from django.shortcuts import render, get_object_or_404, redirect, reverse
from queryset_sequence import QuerySetSequence
from django.contrib import messages
from django.db.models import Q
from .models import Course, Apparel


# ------ All Products ------


def all_products(request):
    """
    Returns all products
    ref: https://pypi.org/project/django-querysetsequence/
    """

    courses = Course.objects.all()
    apparel = Apparel.objects.all()
    products = QuerySetSequence(Course.objects.all(), Apparel.objects.all())

    context = {
        'products': products,
        'courses': courses,
        'apparel': apparel,
    }

    return render(request, 'shop/shop_products.html', context)


def search(request):
    """
    Search page functionality.
    Returns results
    Edited from Boutique Ado Mini Project
    """

    courses = Course.objects.all()
    products = QuerySetSequence(Course.objects.all(), Apparel.objects.all())

    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('search'))

            queries = Q(
                        name__icontains=query) | Q(
                        description__icontains=query
                        )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'courses': courses,
    }

    return render(request, 'shop/search_shop.html', context)


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


def course_detail(request, course_id):
    """
    Returns specified course
    """
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course
    }

    return render(request, 'shop/course_detail.html', context)


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


def apparel_detail(request, apparel_id):
    """
    Returns specified apparel
    """
    apparel = get_object_or_404(Apparel, pk=apparel_id)

    context = {
        'apparel': apparel
    }

    return render(request, 'shop/apparel_detail.html', context)

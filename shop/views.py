from django.shortcuts import render
from .models import Course, Apparel


def all_courses(request):
    """
    Returns All Courses
    """

    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'shop/all_courses.html', context)


def all_apparel(request):
    """
    Returns All Apparel
    """

    apparel = Apparel.objects.all()

    context = {
        'apparel': apparel
    }

    return render(request, 'shop/all_apparel.html', context)

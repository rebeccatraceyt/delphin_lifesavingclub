from django.shortcuts import render
from .models import Course, Apparel


def all_courses(request):
    """
    Returns All Apparel
    """

    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'shop/all_courses.html', context)

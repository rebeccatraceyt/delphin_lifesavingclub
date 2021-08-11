from django.shortcuts import render
from .models import SwimProgramme


def view_home(request):
    """
    Returns homepage
    """
    context = {
        'active_page': 'home',
    }
    return render(request, 'index.html', context)


def view_contact(request):
    """
    Returns homepage
    """
    context = {
        'active_page': 'contact',
    }
    return render(request, 'contact.html', context)


def view_programme(request):
    """
    Returns Learn To Swim Programme Page
    """
    programmes = SwimProgramme.objects.all()

    context = {
        'programmes': programmes,
    }
    return render(request, 'swim_programme.html', context)

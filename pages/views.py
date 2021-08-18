from django.shortcuts import render
from .models import SwimProgramme, FAQ


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


def view_faqs(request):
    """
    Returns FAQs Page
    """
    questions = FAQ.objects.all()

    context = {
        'questions': questions,
    }
    return render(request, 'faqs.html', context)


def view_ethos(request):
    """
    Returns Club Ethos Page
    """
    context = {
        'active_page': 'ethos',
    }
    return render(request, 'ethos.html', context)

from django.shortcuts import render


def view_home(request):
    """
    Returns homepage
    """
    context = {
        'active_page': 'home',
    }
    return render(request, 'index.html', context)


def view_programme(request):
    """
    Returns Learn To Swim Programme Page
    """
    context = {
        'active_page': 'swim_programme',
    }
    return render(request, 'swim_programme.html', context)

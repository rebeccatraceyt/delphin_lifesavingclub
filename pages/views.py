from django.shortcuts import render


def view_home(request):
    """
    Returns homepage
    """
    context = {
        'active_page': 'home',
    }
    return render(request, 'index.html', context)

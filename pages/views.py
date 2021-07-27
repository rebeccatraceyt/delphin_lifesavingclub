from django.shortcuts import render


def view_home(request):
    """
    Returns homepage
    """
    return render(request, 'index.html')

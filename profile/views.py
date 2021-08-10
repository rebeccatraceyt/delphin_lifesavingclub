from django.shortcuts import render


def profile(request):
    """ Display user profile """

    context = {}

    return render(request, 'profile/user_profile.html', context)

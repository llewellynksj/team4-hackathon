from django.shortcuts import render


def display_home(request):
    return render(request, 'home.html', {})


def display_team(request):
    return render(request, 'team.html', {})


def display_contact(request):
    return render(request, 'contact.html', {})

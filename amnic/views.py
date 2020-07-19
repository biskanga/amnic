from django.shortcuts import render

def index(request):
    return render (request, 'amnic/index.html')

def about(request):
    return render (request, 'amnic/about.html')

def team(request):
    return render (request, 'amnic/team.html')

def contact(request):
    return render (request, 'amnic/contact.html')

def activities(request):
    return render (request, 'amnic/activities.html')


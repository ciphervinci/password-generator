from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 10))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    special_characters = request.GET.get('special')

    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if numbers:
        characters.extend(list('1234567890'))
    if special_characters:
        characters.extend(list('!@#$%^&*+-'))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
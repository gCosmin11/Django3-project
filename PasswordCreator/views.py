

from django.shortcuts import render
from django.http import HttpResponse
import random

def home (request):
    return render(request, 'PasswordCreator/home.html')
def password (request):

    thepassword = ''

    characters = list('abcdefghijklmopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get('special'):
        characters.extend("#+*~.:,;-_<>|²³?=/&%$§!")
    if request.GET.get('numbers'):
        characters.extend("1234567890")

    length = int(request.GET.get('length', 12))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'PasswordCreator/password.html', {'password':thepassword})

def about (request):
    return render(request, 'PasswordCreator/about.html')

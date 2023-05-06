from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import UserRegistrationForm, SignUpForm, AddPrograms

from .models import Customer, Programs, SignedProgram

@login_required
def home_view(request):
    return render(request, 'gym_home/home.html', {})

def base_view(request):
    return render(request, 'gym_home/base.html', {})

@login_required
def programs_view(request):
    programs = Programs.objects.all()
    signedPrograms = SignedProgram.objects.all()
    context = {
        'myPrograms': programs,
        'mySignedPrograms': signedPrograms,
    }     
    return render(request, 'gym_home/programs.html', context)

@login_required
def addprograms_view(request):
    programs = Programs.objects.all()
    form = AddPrograms()
    if request.method == "POST":
        form = AddPrograms(request.POST)
        if form.is_valid():
            programTitle = request.POST.get('title')
            programDesc = request.POST.get('description')
            programTimings = request.POST.get('timings')
            Programs.objects.create(title = programTitle, description = programDesc, timings = programTimings)
            return redirect('addprograms')
        else:
            form = AddPrograms()
    context = {
        'form':form,
        'myPrograms': programs
    }
    return render(request, 'gym_home/addprograms.html', context)

@login_required
def signup_view(request):
    programs = Programs.objects.all() 
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data.get('first_name')
            lastName = form.cleaned_data.get('last_name')
            programname = form.cleaned_data.get('program')
            SignedProgram.objects.create(firstname = firstName, lastname = lastName, programName = programname)
            return redirect('programs')
        else:
            form = SignUpForm()
    context = {
        'form':form,
        'myPrograms': programs
    }
    return render(request, 'gym_home/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is None:
            context = {
                'error': 'Username or Password is invalid'
            }
            return render(request, 'gym_home/login.html', context)
        login(request, user)
        return redirect('home')
    context = {}
    return render(request, 'gym_home/login.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'gym_home/logout.html')

def register_user(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'gym_home/register.html', context)
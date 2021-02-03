from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html', {}) 

def create_quiz(request):
    return render(request, 'create_quiz.html', {}) 

def join_quiz(request):
    return render(request, 'join_quiz.html', {})         
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_quiz.html', views.create_quiz, name="create_quiz"),
    path('join_quiz.html', views.join_quiz, name="join_quiz"),
    ]    
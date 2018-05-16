from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegistrationAPI.as_view()),
]

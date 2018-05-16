from django.urls import path
from . import views


urlpatterns = [
    path('list_category', views.ListCategories.as_view()),
    path('start/', views.StartQuiz.as_view()),
    path('start/<int:category_id>/', views.StartQuiz.as_view()),
]

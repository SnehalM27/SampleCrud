from django.urls import path
from .views import add_student_api, student_particular


urlpatterns = [
    path('add/', add_student_api),
    path('particular/<int:pk>/', student_particular),
]
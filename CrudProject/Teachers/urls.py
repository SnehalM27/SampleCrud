from django.urls import path
from .views import TeacherAPIView, TeacherDetailAPIView


urlpatterns = [
    path('create_teacher/', TeacherAPIView.as_view()),
    path('update_teacher/<int:pk>', TeacherDetailAPIView.as_view())
]
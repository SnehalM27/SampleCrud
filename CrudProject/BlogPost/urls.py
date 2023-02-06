from django.urls import path
from .views import BlogGenericAPI, BlogPostDetailView, BlogDetailCombineView


urlpatterns = [
    path('create/', BlogGenericAPI.as_view()),
    path('detail1/<int:pk>/', BlogPostDetailView.as_view()),
    path('detail2/<int:pk>/', BlogDetailCombineView.as_view()),
    
]
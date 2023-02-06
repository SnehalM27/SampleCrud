from django.urls import path
from .views import EmployeeCreateViewSet


urlpatterns = [
    path('create/', EmployeeCreateViewSet.as_view({'post':'create', 'get':'list'})),
    path('create/<int:pk>/', EmployeeCreateViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}))
]
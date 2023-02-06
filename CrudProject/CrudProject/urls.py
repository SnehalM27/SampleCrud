from django.contrib import admin
from django.urls import path, include
from Employees.views import EmployeeModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('emp', EmployeeModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('Students.urls')),
    path('teacher/', include('Teachers.urls')),
    path('blog/', include('BlogPost.urls')),
    path('employee/', include('Employees.urls')),
    path('emp/', include(router.urls))
    
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('universities/', views.UniversityListView.as_view(), name='university_list'),
    path('universities/<int:pk>/', views.UniversityDetailView.as_view(), name='university_detail'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]

from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/universities/')),
    path('universities/', views.UniversityListView.as_view(), name='university_list'),
    path('universities/<int:pk>/', views.UniversityDetailView.as_view(), name='university_detail'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('universities/create/', views.UniversityCreateView.as_view(), name='university_create'),
    path('universities/<int:pk>/update/', views.UniversityUpdateView.as_view(), name='university_update'),
    path('universities/<int:pk>/delete/', views.UniversityDeleteView.as_view(), name='university_delete'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]

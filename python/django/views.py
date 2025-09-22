from django.views.generic import ListView, DetailView
from .models import University, Student

class UniversityListView(ListView):
    model = University
    template_name = 'university_list.html'
    context_object_name = 'universities'

class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'
    context_object_name = 'university'

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import University, Student
from django.urls import reverse_lazy

class UniversityListView(ListView):
    model = University
    template_name = 'university_list.html'
    context_object_name = 'universities'

class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'
    context_object_name = 'university'

class UniversityCreateView(CreateView):
    model = University
    fields = ['full_name', 'short_name', 'established_date']
    template_name = 'university_form.html'
    success_url = reverse_lazy('university_list')

class UniversityUpdateView(UpdateView):
    model = University
    fields = ['full_name', 'short_name', 'established_date']
    template_name = 'university_form.html'
    success_url = reverse_lazy('university_list')

class UniversityDeleteView(DeleteView):
    model = University
    template_name = 'university_confirm_delete.html'
    success_url = reverse_lazy('university_list')

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    fields = ['full_name', 'birth_date', 'university', 'enrollment_year']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['full_name', 'birth_date', 'university', 'enrollment_year']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

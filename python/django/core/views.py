from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import University, Student
from django.urls import reverse_lazy
from .forms import UniversityForm
from django.db.models import Q

class UniversityListView(ListView):
    model = University
    template_name = 'university_list.html'
    context_object_name = 'universities'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return University.objects.filter(
                Q(full_name__icontains=query) | Q(short_name__icontains=query)
            )
        return super().get_queryset()

class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'
    context_object_name = 'university'

class UniversityCreateView(CreateView):
    model = University
    form_class = UniversityForm
    template_name = 'university_form.html'
    success_url = reverse_lazy('university_list')

class UniversityUpdateView(UpdateView):
    model = University
    form_class = UniversityForm
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

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(
                Q(full_name__icontains=query) | Q(university__full_name__icontains=query)
            )
        return super().get_queryset()

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    fields = ['full_name', 'birth_date', 'university', 'enrollment_year']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['full_name', 'birth_date', 'university', 'enrollment_year']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

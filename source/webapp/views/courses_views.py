from django.conf import settings
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from webapp.models import Course
from webapp.forms import CourseForm


class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'courses/create.html'
    form_class = CourseForm
    model = Course
    pk_url_kwarg = 'course_pk'
    permission_required = 'webapp.add_course'

    def get_form(self, form_class=None):
        form = super().get_form()
        return form


class CoursesListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/courses_list.html'
    paginate_by = 6


class CourseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/detail.html'
    pk_url_kwarg = 'course_pk'
    permission_required = 'webapp.view_course'

    def has_permission(self):
        course = self.get_object()
        group_students = course.group.values_list('students', flat=True)
        print(group_students)
        return super().has_permission() and self.get_object().teacher == self.request.user or self.request.user.pk in group_students


class CourseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView): 
    model = Course 
    template_name = 'courses/delete.html'
    success_url = reverse_lazy('webapp:courses_list')
    permission_required = 'webapp.delete_course'

    def has_permission(self):
        course = self.get_object()
        group_students = course.group.values_list('students', flat=True)
        print(group_students)
        return super().has_permission() and self.get_object().teacher == self.request.user or self.request.user.pk in group_students


class CourseEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Course
    fields = ['title', 'description', 'start_date']
    template_name = 'courses/edit.html'
    permission_required = 'webapp.change_course'

    def has_permission(self):
        course = self.get_object()
        group_students = course.group.values_list('students', flat=True)
        print(group_students)
        return super().has_permission() and self.get_object().teacher == self.request.user or self.request.user.pk in group_students

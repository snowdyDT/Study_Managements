from django.shortcuts import get_object_or_404, redirect 
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from webapp.models import Class, Course


class CreateClassView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Class
    fields = ['title', 'description', 'file']
    template_name = 'classes/create.html'
    permission_required = 'webapp.add_class'
    
    def get_context_data(self,**kwargs):
        kwargs['course_pk']=self.kwargs.get('course_pk')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        course_pk = self.kwargs.get('course_pk')
        course = get_object_or_404(Course, pk=course_pk)
        classweek = form.save()
        course.courses.add(classweek)
        return redirect("webapp:course_detail", course_pk=course.pk)


class EditClassView(UpdateView):
    pass


class DeleteClassView(DeleteView):
    pass

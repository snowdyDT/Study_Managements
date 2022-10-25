from django import forms 
from .models import Course, Class


class CourseForm(forms.ModelForm):
    class Meta: 
        model = Course
        fields = ['title', 'description', 'group', 'teacher', 'start_date']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['title', 'description', 'file']

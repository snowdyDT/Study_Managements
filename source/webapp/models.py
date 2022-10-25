from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User  
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    description = models.TextField(max_length=2000, verbose_name='description')
    group = models.ManyToManyField('webapp.Group', verbose_name='group', related_name='groups')
    teacher = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, verbose_name='teacher', default=1)
    start_date = models.DateField(('Start date'), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("webapp:course_detail", args=[str(self.id)])


class Group(models.Model):
    group_name = models.CharField(max_length=50, verbose_name='group_name')
    specialization = models.ForeignKey('webapp.Specialization', on_delete=models.CASCADE, verbose_name='specialization')
    students = models.ManyToManyField(get_user_model(), verbose_name='students', related_name='students')

    def __str__(self):
        return self.group_name


class Class(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    description = models.TextField(max_length=2000, verbose_name='description')
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ManyToManyField('webapp.Course', verbose_name='course', related_name='courses')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("webapp:course_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


class Specialization(models.Model):
    spec_name = models.CharField(max_length=100, verbose_name='spec_name')

    def __str__(self):
        return self.spec_name
    
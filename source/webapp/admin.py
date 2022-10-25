from django.contrib import admin
from .models import Course, Group, Class, Specialization


models = [Course, Group, Class, Specialization]
for model in models:
    admin.site.register(model)
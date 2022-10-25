from django.urls import path
from webapp import views as webapp_views

app_name = "webapp"

urlpatterns = [
    path('', webapp_views.CoursesListView.as_view(), name='courses_list'),
    path('course/<int:course_pk>/', webapp_views.CourseDetailView.as_view(), name='course_detail'), 
    path('course/<int:pk>/delete/', webapp_views.CourseDeleteView.as_view(), name='course_delete'), 
    path('course/new/', webapp_views.CourseCreateView.as_view(), name='course_create'), 
    path('course/<int:pk>/edit/', webapp_views.CourseEditView.as_view(), name='course_edit'),

    path('course/<int:course_pk>/class/new', webapp_views.CreateClassView.as_view(), name='class_create'),
    path('course/<int:course_pk>/class/delete', webapp_views.DeleteClassView.as_view(), name='class_delete')
]
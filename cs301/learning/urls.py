from django.urls import path
from . import views

urlpatterns = [
    path('', views.variable_view, name='variableAndConstantView'),
    #path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    #path('course/<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    #path('course/<int:course_id>/complete/', views.complete_course, name='complete_course'),
    #path('courses/', views.all_courses, name='all_courses'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('pupils', views.showPupils, name='pupils'),
    path('pupils/<str:pk>/', views.showPupil, name='show_pupil'),
    path('students', views.showStudents, name='students'),
    path('students/<str:pk>/', views.showStudent, name='show_student'),
]

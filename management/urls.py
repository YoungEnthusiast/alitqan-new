from django.urls import path
from . import views

urlpatterns = [
    path('a---n/sessions', views.showSessionsFirst, name='sessions_first'),
    path('a---n/classes', views.showClassesFirst, name='classes_first'),
    path('a---n/subjects', views.showSubjectsFirst, name='subjects_first'),
    path('a---n/session/update/<int:id>', views.updateSessionFirst, name='session_update_first'),
    path('a---n/session/add-new', views.addSession, name='session_first'),
    path('a---n/class/add-new', views.addClass, name='class_first'),
    path('a---n/subject/add-new', views.addSubject, name='subject_first'),
    path('a---n/class/update/<int:id>', views.updateClassFirst, name='class_update_first'),
    path('a---n/subject/update/<int:id>', views.updateSubjectFirst, name='subject_update_first'),
    path('a---n/session/delete/<int:id>', views.deleteSessionFirst),
    path('a---n/class/delete/<int:id>', views.deleteClassFirst),
    path('a---n/subject/delete/<int:id>', views.deleteSubjectFirst),
]

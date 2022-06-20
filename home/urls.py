from django.urls import path
from . import views

urlpatterns = [
    path('', views.showHome, name='index'),
    path('admission', views.showAdmission, name='admission'),
    path('about-alitqan', views.showAbout, name='about'),
    path('contact-us', views.showContact, name='contact'),
]

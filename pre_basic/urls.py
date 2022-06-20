from django.urls import path
from . import views

urlpatterns = [
    path('staff/pre-basic/first-term', views.showFirsts, name='firsts'),
    path('parents/pre-basic/first-term', views.showFirstsUser, name='firsts_user'),
    path('staff/pre-basic/first-term/<int:pk>/', views.showFirst, name='show_first'),
    path('parents/pre-basic/first-term/<int:pk>/', views.showFirstUser, name='show_first_user'),
    path('staff/pre-basic/first-term/update/<int:id>', views.updateFirsts, name='firsts_update'),
    path('staff/pre-basic/first-term/add-scores', views.addFirst, name='pre_basic_first'),
    path('staff/pre-basic/second-term', views.showSeconds, name='seconds'),
    path('parents/pre-basic/second-term', views.showSecondsUser, name='seconds_user'),
    path('staff/pre-basic/second-term/<int:pk>/', views.showSecond, name='show_second'),
    path('parents/pre-basic/second-term/<int:pk>/', views.showSecondUser, name='show_second_user'),
    path('staff/pre-basic/second-term/update/<int:id>', views.updateSeconds, name='seconds_update'),
    path('staff/pre-basic/second-term/add-scores', views.addSecond, name='pre_basic_second'),
    path('staff/pre-basic/third-term', views.showThirds, name='thirds'),
    path('parents/pre-basic/third-term', views.showThirdsUser, name='thirds_user'),
    path('staff/pre-basic/third-term/<int:pk>/', views.showThird, name='show_third'),
    path('parents/pre-basic/third-term/<int:pk>/', views.showThirdUser, name='show_third_user'),
    path('staff/pre-basic/third-term/update/<int:id>', views.updateThirds, name='thirds_update'),
    path('staff/pre-basic/third-term/add-scores', views.addThird, name='pre_basic_third'),
]

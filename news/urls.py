from django.urls import path
from . import views
#from treatment import views as treatment_views

urlpatterns = [
    path('news-and-events', views.showEvents, name='events'),
    path('a---n/news', views.showEventsFirst, name='events_first'),
    path('a---n/news/add-new', views.addEvent, name='event_first'),
    path('a---n/news/update/<int:id>', views.updateEventFirst, name='event_update_first'),
    path('a---n/news/delete/<int:id>', views.deleteEventFirst),
]

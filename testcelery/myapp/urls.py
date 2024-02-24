from .views import notifiction_view_function 
from django.urls import path

urlpatterns = [
    path('myapp/', notifiction_view_function, name='trigger_task'),
] 
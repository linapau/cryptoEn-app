from django.urls import path
from . import views

# defines a new URL pattern that maps to the function in api/views.py
urlpatterns = [
    path('hello-world/', views.siema, name='siema'),
]
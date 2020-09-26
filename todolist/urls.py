from django.urls import path
from . import views

urlpatterns = [
    path("practice_loop", views.practice_loop, name="practice_loop")
]
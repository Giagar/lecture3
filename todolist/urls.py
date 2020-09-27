from django.urls import path
from . import views

app_name = "todolist"
urlpatterns = [
    path("practice_loop", views.practice_loop, name="practice_loop"),
    path("practice_template_page1", views.practice_template_page1, name="practice_template_page1"),
    path("practice_template_page2", views.practice_template_page2, name="practice_template_page2"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path('projects', views.project_list, name='portfolio-projects'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('works.html', views.project_index, name="project_index"),
    path('about.html', views.about, name="about"),
]
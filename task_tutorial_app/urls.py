from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='task-index'),
    path('about/', views.about, name='task-about')
]
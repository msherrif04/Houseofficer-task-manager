from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('beds/', views.getBeds),
    path('beds/add/', views.addBed),
    path('beds/<str:pk>/update', views.updateBed),
    path('beds/<str:pk>/tasks', views.getBedTasks),
    path('beds/<str:pk>/delete', views.deleteBed),
    path('beds/<str:pk>/', views.getBedDetails),
         
    path('tasks/', views.getTasks),
    path('tasks/add/', views.addTask),
    path('tasks/pending/', views.getPendingTasks),
    path('tasks/completed/', views.getCompletedTasks),
    path('tasks/<str:pk>/update', views.updateBed),
    path('tasks/<str:pk>/delete', views.deleteTask),


]
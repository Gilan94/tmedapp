from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
	path('client-create/', views.clientCreate, name="client-create"),
	path('client-list/', views.clientsList, name="client list"),
	path('client-edit/<str:pk>/', views.clientEdit, name="client edit"),
	path('client-detail/<str:pk>/', views.clientDetail, name="client detail"),
	path('schedule-list/<str:pk>/', views.schedulesList, name="schedule-list"),
] 

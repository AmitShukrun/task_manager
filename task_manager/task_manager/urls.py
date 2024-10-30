from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskListCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]

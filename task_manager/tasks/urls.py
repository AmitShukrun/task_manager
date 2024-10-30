from django.urls import path
from .views import AllTasks, CreateTask, TaskDetail

urlpatterns = [
    path('', AllTasks.as_view(), name='task-list'),  # Route for listing all tasks (GET)
    path('create/', CreateTask.as_view(), name='task-create'),  # Route for creating a task (POST)
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail'),  # Route for specific task (GET, PUT, DELETE)
]

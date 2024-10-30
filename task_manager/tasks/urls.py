from django.urls import path
from .views import AllTasks, TaskListCreate, TaskDetail

urlpatterns = [
    path('', AllTasks.as_view(), name='task-list'),  # Route for listing all tasks (GET)
    path('create/', TaskListCreate.as_view(), name='task-create'),  # Route for creating a task (POST)
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail'),  # Route for specific task (GET, PUT, DELETE)
]

import subprocess
from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'tasks'

    def ready(self):
        # Used to run the task_client.py script when the application up
        try:
            subprocess.Popen(["python", "tasks/task_client.py"])
        except Exception as e:
            print("Error running task_client.py:", e)

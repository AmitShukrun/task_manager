from django.apps import AppConfig
import subprocess


class TaskConfig(AppConfig):
    name = 'task'

    def ready(self):
        # Used to run the task_client.py script when the application up
        try:
            subprocess.Popen(["python", "task/task_client.py"])
        except Exception as e:
            print("Error running task_client.py:", e)

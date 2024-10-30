import subprocess
from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'tasks'

    def ready(self):
        # This setup runs task_client.py only for this homework assignment.
        # In a production environment, I would never include this; it's just a substitute for Postman.
        try:
            subprocess.Popen(["python", "tasks/task_client.py"])
        except Exception as e:
            print("Error running task_client.py:", e)

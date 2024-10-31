from django.apps import AppConfig


# class TaskConfig(AppConfig):
#     name = 'tasks'
#
#     def ready(self):
#         # Code has been disabled
#         pass


import subprocess
import time
import requests
from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'tasks'

    # def ready(self):
    #     # This setup runs task_client.py only for this homework assignment.
    #     # In a production environment, I would never include this; it's just a substitute for Postman.
    #
    #     # Run the Django server in a separate process
    #     server_process = subprocess.Popen(["python", "manage.py", "runserver", "0.0.0.0:8000"])
    #
    #     # Check if the server is up
    #     while True:
    #         try:
    #             # Send a request to check if the server is available
    #             response = requests.get('http://localhost:8000/tasks')
    #             # response = requests.get('http://db:8000/tasks')
    #             if response.status_code == 200:
    #                 print("Server is up and running.")
    #                 break  # Exit loop if server is available
    #         except requests.exceptions.ConnectionError:
    #             print("Waiting for the server to be available...")
    #
    #         # Wait 10 seconds before checking again
    #         time.sleep(10)
    #
    #     # Run task_client.py
    #     try:
    #         subprocess.Popen(["python", "tasks/task_client.py"])
    #     except Exception as e:
    #         print("Error running task_client.py:", e)

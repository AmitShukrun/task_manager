import requests


def run_task_client():
    base_url = "http://localhost:8000/tasks/"

    # # Create new task
    # task_data = {"title": "Example Task", "description": "This is an example task.", "completed": False}
    # response = requests.post(f"{base_url}create/", json=task_data)
    # print("Create Task:", response.json())

    # # Get all tasks
    # response = requests.get(base_url)
    # print("All Tasks:", response.json())

    task_id = 4

    # # Update task
    # updated_task_data = {"title": "Updated Task", "description": "Updated description.", "completed": True}
    # response = requests.put(f"{base_url}{task_id}/", json=updated_task_data)
    # print("Update Task:", response.json())

    # Delete Task
    response = requests.delete(f"{base_url}{task_id}/")
    print("Delete Task:", response.status_code)


if __name__ == "__main__":
    run_task_client()

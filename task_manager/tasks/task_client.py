import requests


def run_task_client():
    # base_url = "http://localhost:8000/tasks/"
    # base_url = "http://127.0.0.1:8000/tasks/"
    base_url = "http://web:8000/tasks/"

    # Create new task
    task_data = {"title": "Example Task", "description": "Example task.", "completed": False}
    response = requests.post(f"{base_url}create/", json=task_data)
    print("Create Task:", response.json())

    # # Get all tasks
    # response = requests.get(base_url)
    # print("All Tasks:", response.json())

    # # Get tasks by filter
    # search_term = "example"  # Enter the words you want to search from all the tasks in the description column
    # response_filtered = requests.get(f"{base_url}?search={search_term}")
    # print(f"Filtered Tasks (searching for '{search_term}') in description column:\n", response_filtered.json())
    #
    # # Get tasks by category filter
    # search_category = "urgent"
    # response_filtered = requests.get(f"{base_url}?category={search_category}")
    # print(f"Filtered Tasks (searching for '{search_category}') in category column:\n", response_filtered.json())

    # # Get completed tasks filter
    # completed = True
    # response_filtered = requests.get(f"{base_url}?completed={completed}")
    # print(f"Filtered Tasks searching for completed tasks:\n", response_filtered.json())

    task_id = 1

    # # Update task
    # updated_task_data = {"title": "Updated Task", "description": "Updated description.", "completed": True}
    # response = requests.put(f"{base_url}{task_id}/", json=updated_task_data)
    # print("Update Task:", response.json())

    # # Delete Task
    # response = requests.delete(f"{base_url}{task_id}/")
    # print("Delete Task:", response.status_code)


if __name__ == "__main__":
    run_task_client()

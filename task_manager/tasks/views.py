from .models import Task
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class AllTasks(APIView):
    def get(self, request):
        """
        Returns all existing tasks from the database.
        """
        try:
            search_term = request.query_params.get('search', None)
            category = request.query_params.get('category', None)

            if search_term:
                # icontains is actually a case-insensitive search
                tasks = Task.objects.filter(description__icontains=search_term)
            else:
                tasks = Task.objects.all()

            if category:
                tasks = tasks.filter(categories__icontains=category)

            serializer = TaskSerializer(tasks, many=True)  # Serialize the task data
            return Response(serializer.data)  # Return the serialized data
        except Exception as e:
            # Return a 500 error if any exception occurs
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateTask(APIView):
    """
    Handles creating a new task with provided data.
    """
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):

    def get(self, request, pk):
        """Retrieve a task by its primary key (pk)."""
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        """Update a task's details by its primary key (pk)."""
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        """Delete a task by its primary key (pk)."""
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

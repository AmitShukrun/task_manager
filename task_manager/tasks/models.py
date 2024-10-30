from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'task'

    def __str__(self):
        return self.title

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    categories = models.CharField(max_length=25, blank=True)

    class Meta:
        db_table = 'task'

    def __str__(self):
        return self.title

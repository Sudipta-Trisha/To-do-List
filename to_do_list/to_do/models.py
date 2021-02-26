from django.db import models

class Task(models.Model):
    item = models.CharField(max_length=50)
    details = models.TextField(max_length=300)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item

from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title



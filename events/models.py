from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()

    def __str__(self):
        return self.name

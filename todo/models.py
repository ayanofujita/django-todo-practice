from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=0)
    progress = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

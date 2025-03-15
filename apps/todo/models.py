from django.db import models

# Create your models here.

class Todo(models.Model):
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    text = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text
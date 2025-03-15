from django.db import models

# Create your models here.

class todo(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    text = models.TextField()
    done = models.BooleanField()

    def __str__(self):
        return self.text
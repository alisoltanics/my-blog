from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=350
    )
    description = models.TextField()

    def __str__(self):
        return self.title

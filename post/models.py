from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


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
    image = models.ImageField(
        upload_to="post/images",
        blank=True, null=True,
        max_length=300
    )

    def __str__(self):
        return self.title

    @property
    def image_absolute_url(self):
        if self.image:
            return "{}{}".format(settings.DOMAIN, self.image.url)
        return None

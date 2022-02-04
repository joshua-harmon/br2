from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    content = models.CharField(max_length=300)
    created = models.DateTimeField(editable=False)
    archived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
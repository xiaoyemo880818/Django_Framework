from django.db import models
from django.conf import settings
from django.utils import timezone
# Once created a model, Django provides API to operate database to CRUD records.

# class Post extends class Model
# a model represent a table in database
# Django doesn't hit the database until you explicitly call save().
class Post(models.Model):
    # attributes represent columns
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # use print(object) will print the object title
    def __str__(self):
        return self.title
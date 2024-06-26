from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    summary = models.TextField(max_length=200)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.author})"

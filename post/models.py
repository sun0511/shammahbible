from django.db import models

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True)
    text = models.TextField(blank=True)
    audio = models.FileField(blank=True)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
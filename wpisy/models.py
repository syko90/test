from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wpis(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.title

    def przycinanie(self):
        return self.body[:50] + '...'


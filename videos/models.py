from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):

    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)
    class Meta:
        ordering = ['-added']


class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + ' ' + self.lname


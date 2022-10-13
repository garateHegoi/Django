from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    prezioa = models.IntegerField(null=True)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return u'%s' % self.title, self.author, self.prezioa, self.text
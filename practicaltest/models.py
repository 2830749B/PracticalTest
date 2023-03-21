from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    description = models.CharField(max_length=128)


    def __str__(self):
        return self.title
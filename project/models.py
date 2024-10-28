from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_ad = models.DateTimeField(auto_now_add=True)
    isbn = models.CharField(max_length=13)
    count_page = models.IntegerField
    language = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)


def __str__(self):
    return self.title

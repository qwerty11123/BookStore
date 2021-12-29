from django.db import models
from django.contrib.auth.models import User
# Create your models here.


booktype = [
    ['Physical','Physical'],['Ebook','Ebook']
]

class Genre(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Genre,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    book_type = models.CharField(max_length=100,null=True,choices=booktype)
    description = models.TextField(null=True)
    favbook = models.BooleanField(default=False)


    def __str__(self):
        return self.title






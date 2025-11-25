from django.db import models
from .querysets import UserQuerySet
from datetime import datetime


# Create your models here.
class User(models.Model):       
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    hobby = models.CharField(max_length=200, null=True)

    objects = UserQuerySet.as_manager()

    def __str__(self):
        return f'nome: {self.name} cognome: {self.surname} age: {self.age}'
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')
    image = models.CharField(null=True)

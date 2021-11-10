from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Make(models.Model):
    name_text = models.CharField(max_length=100)

    def __str__(self):
        return self.name_text


class Autos(models.Model):
    nickname = models.CharField(max_length=100)
    make = models.ForeignKey(Make, on_delete=CASCADE)
    milage = models.IntegerField(default=0)
    comments = models.CharField(max_length=1000)


    
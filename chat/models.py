from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sick(models.Model):
    username = models.CharField( max_length=400)
    age = models.IntegerField(default=0)
    is_xuruj = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_times = models.DateTimeField(auto_now_add=True)
    dori_name = models.CharField( max_length=400)
    dori_miqdor = models.CharField( max_length=400)
    xulosa = models.CharField( max_length=400)
    def __str__(self):
        return self.username


class Hurujs(models.Model):
    date_times = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(Sick, on_delete=models.CASCADE,related_name='persons' )
    









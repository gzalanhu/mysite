from django.db import models

# Create your models here.
class Progame(models.Model):
    AppName = models.CharField(max_length=50)
    ProName = models.CharField(max_length=40)
    Domain = models.CharField(max_length=100)
    Apptype = models.CharField(max_length=40)

    def __unicode__(self):
        return self.AppName


class UserType(models.Model):
    name = models.CharField(max_length=50)

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    user_type =  models.ForeignKey('UserType')
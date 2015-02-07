from django.db import models

class About(models.Model):
    tel = models.CharField(max_length = 200)
    qq = models.CharField(max_length = 200)
    address = models.TextField()
    email = models.EmailField()
    fax = models.CharField(max_length = 200)

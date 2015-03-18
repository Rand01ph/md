from django.db import models


class About(models.Model):
    tel = models.CharField(max_length = 200)
    qq = models.CharField(max_length = 200)
    address = models.URLField()
    email = models.EmailField()
    fax = models.CharField(max_length = 200)


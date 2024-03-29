from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Site(models.Model):
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.url
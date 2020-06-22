from django.db import models

# Create your models here.
""" шаблонная модель """

class TestUser(models.Model):
    username = models.CharField(max_length=120)

    def __str__(self):
        return self.username

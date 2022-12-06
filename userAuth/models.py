from django.db import models

# Create your models here.
class GetData(models.Model):
    username=models.CharField("usename",max_length=50)
    password=models.CharField("password",max_length=50)

    def __str__(self):
        return self.username
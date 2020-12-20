from django.db import models


# Create your models here.

class User_mail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=80, blank=False)
    subject = models.TextField(max_length=50, blank=True)
    message = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.email)

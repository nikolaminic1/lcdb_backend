from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    comment = models.TextField(max_length=1000, null=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname

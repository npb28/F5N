from django.conf import settings
from django.db import models


# Creat a contact object that holds first/last name and number
class Contact(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    # Returns contact's last name in string from
    def __str__(self):
        return self.last_name

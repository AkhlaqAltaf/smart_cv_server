from django.contrib.auth.models import User
from django.db import models


class HostDetails(models.Model):
    hostname = models.CharField(max_length=50)
    host_email = models.EmailField()
    host_phone_number = models.CharField(max_length=50)
    host_address = models.CharField(max_length=100)

    def __str__(self):
        return self.hostname


class EventDetails(models.Model):
    event_type = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=100)

    def __str__(self):
        return self.event_type


class MessageDetails(models.Model):
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.message


class Invitation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    event = models.ForeignKey(EventDetails, on_delete=models.CASCADE)
    host = models.ForeignKey(HostDetails, on_delete=models.CASCADE)
    message = models.ForeignKey(MessageDetails, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.event_type

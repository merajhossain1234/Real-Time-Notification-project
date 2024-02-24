# models.py

from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.id}: {self.message}"

class DayUserAssociation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])

    class Meta:
        unique_together = ['user', 'day']

    def __str__(self):
        return f"{self.user.username}'s association on {self.day}"


class Market(models.Model):
    marketuser = models.ForeignKey(DayUserAssociation,on_delete=models.SET_NULL, null=True)
    market_items=models.CharField(max_length=200)
    date= models.DateTimeField(auto_now_add=True)
    
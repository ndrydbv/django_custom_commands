from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=20, choices=[('NA', 'North America'), ('EU', 'Europe')])
    region = models.CharField(max_length=2)
    moderator = models.BooleanField()

    def __str__(self):
        return self.name

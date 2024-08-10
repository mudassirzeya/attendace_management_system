from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    super_user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Attendance(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    attendance = models.CharField(max_length=200, null=True, blank=True)
    attend_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.TextField(blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Custom User Model
class IMUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Admin Staff'),
        ('ADMIN', 'Admin'),
    ]
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES)
    date_created = models.DateTimeField(default=timezone.now)

# Cohort Model
class Cohort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohorts')

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='membership')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='created_memberships')
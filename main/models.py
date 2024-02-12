from django.db import models
from users.models import IMUser, Cohort, CohortMember
#  Models 

class Course(models.Model):
    name=models.CharField(max_length=1000)
    date_created= models.DateTimeField(auto_now_add=True,blank=True, null=True)
    date_modified= models.DateTimeField(auto_now=True, blank=True, null=True)

class ClassSchedule(models.Model):
    REPEAT_CHOICES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('NONE', 'None'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=10, choices=REPEAT_CHOICES, default='NONE')
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='organized_classes')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='classes')
    venue = models.CharField(max_length=255)

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name='attendances')
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='attendances')
    is_present = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='attendance_records')

class Query(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DECLINED', 'Declined'),
        ('RESOLVED', 'Resolved'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='assigned_queries')
    resolution_status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='PENDING')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='created_queries')

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='comments_made')
from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display=("name", "date_created", "date_modified")

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date_and_time', 'end_date_and_time', 'is_repeated', 'organizer', 'cohort', 'is_active')
    list_filter = ('is_active', 'is_repeated', 'cohort', 'organizer')
    search_fields = ('title', 'description')

class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display = ('class_schedule', 'attendee', 'is_present', 'date_created', 'author')
    list_filter = ('is_present', 'class_schedule', 'attendee')
    search_fields = ('class_schedule__title', 'attendee__username')

class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'submitted_by', 'assigned_to', 'resolution_status', 'date_created', 'author')
    list_filter = ('resolution_status', 'submitted_by', 'assigned_to')
    search_fields = ('title', 'description')

class QueryCommentAdmin(admin.ModelAdmin):
    list_display = ('query', 'date_created', 'author')
    list_filter = ('date_created', 'author')
    search_fields = ('query__title', 'comment')

    
admin.site.register(Course, CourseAdmin)
admin.site.register(ClassSchedule, ClassScheduleAdmin)
admin.site.register(ClassAttendance, ClassAttendanceAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(QueryComment, QueryCommentAdmin)

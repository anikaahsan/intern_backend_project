from django.contrib import admin
from job.models import Job,Application

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model=Job
    list_display=[field.name for field in Job._meta.fields]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    model=Application
    list_display=[field.name for field in Application._meta.fields]
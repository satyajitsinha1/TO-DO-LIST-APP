from django.contrib import admin
from.models import tasks

# Register your models here.

@admin.register(tasks)
class tasksadmin(admin.ModelAdmin):
    list_display=['id','task','status']

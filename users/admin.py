from django.contrib import admin
from .models import Profile, Skill, Message

# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'is_read')
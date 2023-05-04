from django.contrib import admin
from .models import Project, Review, Tag

# Register your models here.
admin.site.register(Tag)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('value', 'owner', 'project')


@admin.register(Project)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')

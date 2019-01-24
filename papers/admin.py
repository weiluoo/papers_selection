from django.contrib import admin

from .models import Subject, Paper


# Register your models here.
admin.site.register(Subject)


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_subject', 'year')
    list_filter = ('available', )
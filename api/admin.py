from django.contrib import admin
from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_at", "updated"]

admin.site.register(Note, NoteAdmin)
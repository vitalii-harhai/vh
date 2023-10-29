from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('summary', 'label', 'date')
    list_display_links = ('summary',)
    search_fields = ('summary',)


admin.site.register(Note, NoteAdmin)

from django.contrib import admin
from .models import CatalogName, LinkList


class CatalogNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'priority')
    list_display_links = ('name', 'user', 'priority')
    search_fields = ('name',)


class LinkListAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'catalog')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(CatalogName, CatalogNameAdmin)
admin.site.register(LinkList, LinkListAdmin)

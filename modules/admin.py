from django.contrib import admin

from modules.models import Module, Resource, Tag


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('module', 'title', 'added_by', 'type', 'created_at', 'updated_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

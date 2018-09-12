from django.contrib import admin

from modules.models import Module, Video, Tag, Resource


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('module', 'title', 'creator', 'created_at', 'updated_at')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'type')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

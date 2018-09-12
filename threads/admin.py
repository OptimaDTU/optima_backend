from django.contrib import admin

from threads.models import ThreadCategory, Thread, Post, Comment


@admin.register(ThreadCategory)
class ThreadCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'author', 'content', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')

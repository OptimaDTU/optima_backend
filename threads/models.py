from django.db import models

from django.template.defaultfilters import slugify


class ThreadCategory(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)

    class Meta:
        verbose_name_plural = 'Thread Categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ThreadCategory, self).save(*args, **kwargs)


class Thread(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()
    author = models.ForeignKey('accounts.Profile', null=True, on_delete=models.SET_NULL, related_name='threads')
    category = models.ForeignKey('ThreadCategory', null=True, on_delete=models.SET_NULL, related_name='threads')
    slug = models.SlugField(max_length=250, blank=True)
    tags = models.ManyToManyField('modules.Tag', related_name='threads', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Thread, self).save(*args, **kwargs)


class Post(models.Model):
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey('accounts.Profile', null=True, on_delete=models.SET_NULL, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.content


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('accounts.Profile', null=True, on_delete=models.SET_NULL, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.content



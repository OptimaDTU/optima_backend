from django.db import models
from django.template.defaultfilters import slugify

from modules.utils import ResourceTypeChoices


class Module(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    curators = models.ManyToManyField('accounts.Profile', related_name='modules', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Module, self).save(*args, **kwargs)


class Video(models.Model):
    module = models.ForeignKey('Module', null=True, on_delete=models.SET_NULL, related_name='videos')
    creator = models.ForeignKey('accounts.Profile', null=True, on_delete=models.SET_NULL, related_name='videos')
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    next_video = models.OneToOneField('self', blank=True, null=True, on_delete=models.SET_NULL,
                                      related_name='previous_video')
    tags = models.ManyToManyField('Tag', related_name='videos')
    slug = models.SlugField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Video, self).save(*args, **kwargs)


class Resource(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(blank=True, null=True)
    video = models.ForeignKey('Video', null=True, on_delete=models.SET_NULL, related_name='resources')
    type = models.CharField(max_length=100, choices=ResourceTypeChoices)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

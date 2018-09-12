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


class Resource(models.Model):
    module = models.ForeignKey('Module', null=True, on_delete=models.SET_NULL, related_name='resources')
    added_by = models.ForeignKey('accounts.Profile', null=True, on_delete=models.SET_NULL, related_name='resources')
    type = models.CharField(max_length=100, choices=ResourceTypeChoices)
    title = models.CharField(max_length=250)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='resources')
    link = models.URLField(blank=True, null=True)
    rank = models.PositiveIntegerField(default=1)
    slug = models.SlugField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ('rank',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Resource, self).save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

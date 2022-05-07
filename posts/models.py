from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
# from django.core.urlresolvers import reverse

class Post(models.Model):
  name = models.CharField(max_length=224, null=False, blank=False)
  content = models.TextField(max_length=5000, null=False, blank=False)
  slug = models.SlugField(max_length=255)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.content
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super(Post, self).save(*args, **kwargs)
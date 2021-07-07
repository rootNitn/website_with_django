from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
#from froala_editor.fields import FroalaField
from .fun import *

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    slug = models.SlugField(max_length=500, null=True , blank=True)
    image = models.ImageField(("/static/nitin"), upload_to="static/nitin", height_field=None, width_field=None, max_length=None)
    create_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(blog, self).save(*args, **kwargs)

    
    

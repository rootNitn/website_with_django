from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.

class blogmodel(models.Models):
    title = models.CharField(max_length=100)
    content = models.TextField(max_lenght=1000)
    slug = models.SlugField(max_length=500)
    image = models.ImageField(_("/nitin"), upload_to=None, height_field=None, width_field=None, max_length=None)
    create_at = models.models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    upload_to = models.models.DateTimeField(_(""), auto_now=True, auto_now_add=False)

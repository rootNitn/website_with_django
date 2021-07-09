from django.contrib import admin
from blog.models import blog
# Register your models here.
admin.site.register(blog)


#@admin.register(blog)
#class PostAdmin(admin.ModelAdmin):
 #   class Media:
  #      js = ('static/tiny.js')



from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name

class video(models.Model):
    idi = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    le = models.IntegerField()
    def __str__(self):
        return self.idi



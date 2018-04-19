from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='thumbnail/')
    heroimage = models.ImageField(upload_to='heroimage/')
    meta = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    body= models.TextField()

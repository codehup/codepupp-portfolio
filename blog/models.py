from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='thumbnail/')
    heroimage = models.ImageField(upload_to='heroimage/')
    meta = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    body = RichTextUploadingField()

    # def summary(self):
    #     return self.body[:100]
    def __str__(self):
        return self.title
    # def __str__(self):
    #     return self.pub_date

    def pub_date_hooman(self):
        return self.pub_date.strftime('%b %e %Y')

    # def show_latest_post
    #     latest_post = Blog.pub_date
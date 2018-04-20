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

    # def summary(self):
    #     return self.body[:100]
    def __str__(self):
        return self.title
    # def __str__(self):
    #     return self.pub_date

    def pub_date_hooman(self):
        return self.pub_date.strftime('%b %e %Y')

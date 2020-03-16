from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 500)
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='image/')
    body = models.TextField()

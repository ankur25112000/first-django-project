from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='image/')
    body = models.TextField()

def __str__(self):
    return self.title

def summary(self):
    return self.body[ :100]

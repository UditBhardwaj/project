from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# import _datetime
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    datetime = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title
  

    def get_absolute_url(self):
        return reverse('detail',args = (str(self.id)))



class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     
     def __str__(self):
        return "Message from " + self.name + ' - ' + self.email
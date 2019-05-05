from django.db import models

# Create your models here.
class Identity(models.Model):
    username = models.CharField(max_length=200, default="")
    password = models.IntegerField(default="")
    
class Lion(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    ddate = models.DateField(auto_now=False, auto_now_add=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    location = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='images/', blank=True)
    people_count = models.IntegerField(default=0)
    major = models.CharField(max_length = 20, default="")
    view_count = models.IntegerField(default=0) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.title
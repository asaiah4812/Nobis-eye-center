from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=4000, blank=True)
    image = models.ImageField(upload_to='images' )
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class meta:
        verbose_name = ['Service']
        verbose_plural_name = ('Services')
        
    def get_absolute_url(self):
        return reverse('services_detail', args=[self.slug])
    
    
    def __str__(self):
        return self.title
    
    
class Day(models.Model):
    days = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.days

class Doctor(models.Model):
    expert = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    detail = models.TextField(max_length=2000)
    slug = models.SlugField(max_length=100)
    photo = models.ImageField(upload_to='img')
    working_days = models.ForeignKey(Day, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("doctors_detail", args = [self.slug])
    


class Book(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField(max_length=100, blank=True, unique=True)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    msg = models.TextField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.name    
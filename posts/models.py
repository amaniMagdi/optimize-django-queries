from django.db import models

# Create your models here.
class Auther(models.Model):
    name= models.CharField(max_lengh=100) 
    def __str__(self):
        return str(self.name)
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
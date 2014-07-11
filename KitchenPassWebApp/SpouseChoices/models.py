from django.db import models
from gcm.models import AbstractDevice



class SpouseRequest(models.Model):
    question = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return self.question
    
class SpouseResponse(models.Model):
    answer = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.answer
    
 
class UserDevice(AbstractDevice):
    username = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return self.dev_id  

from django.db import models



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
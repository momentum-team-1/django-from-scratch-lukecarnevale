from django.db import models
from users.models import User


# Create your models here.
class Deck (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='decks', null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title



class Card (models.Model):
    deck = models.ForeignKey(to=Deck, on_delete=models.CASCADE, related_name='cards')
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    mastered = models.BooleanField("Mastered", default=False)

    def __str__(self):
        return f"{self.question} {self.answer}" 
        

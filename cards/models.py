from django.db import models
from users.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

# Create your models here.
class Deck (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='decks')
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title} {self.question}"


class Card (models.Model):
    deck = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} {self.answer}"

#add more classes down here, but migrate after creating

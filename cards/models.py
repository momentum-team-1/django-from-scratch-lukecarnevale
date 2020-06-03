from django.db import models
from users.models import User

# Create your models here.
class Deck (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='creator')
    title = models.CharField(max_length=255)
    # card_deck = models.postiveIntegerField(null=True, blank=True)

class Card (models.Model):
    deck = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=255)

#add more classes down here, but migrate after creating

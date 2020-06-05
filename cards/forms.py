from django import forms
from .models import Deck, Card

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'title', 
        ]

class CardForm(forms.ModelForm):
    class Meta:
        model : Card
        fields = [
            'question'
            'answer'
        ]
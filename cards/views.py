from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Deck, Card 
from .forms import DeckForm, CardForm

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='deck_list')

    return render (request, "home.html")

@login_required
def deck_list(request):    
    decks = request.user.decks.all()

    return render(request, 'deck_list.html', {"decks": decks})

@login_required
def deck_detail(request,pk):
    deck = get_object_or_404(request.user.decks, pk=pk)
    return render(request, "deck_detail.html", {"deck": deck})

@login_required
def add_deck(request):
    if request.method == "POST": #submitted the form
        form = DeckForm(data=request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect(to='deck_detail', pk=deck.pk)
    else: #viewing page for the first time
        form = DeckForm()

    return render(request, "add_deck.html", {"form": form})    

@login_required
def add_card(request, pk):
    deck = get_object_or_404(request.user.decks, pk=pk)
    form = CardForm(data=request.POST)
    if form.is_valid():
        card = form.save(commit=False)
        card.deck = deck
        card.save()
        return redirect(to='deck_detail', pk=deck.pk)
    else:
        form = CardForm()

    return render(request, "add_card.html", {
        "form": form,
        "deck": deck,
        })

@login_required
def delete_deck(request, pk):
    deck = get_object_or_404(request.user.decks, pk=pk)
    if request.method == "POST":
        deck.delete()
        return redirect(to='deck_list')

    return render(request, "delete_deck.html", {"deck": deck})   

@login_required
def view_question(request,pk):
    deck = get_object_or_404(request.user.decks, pk=pk)
    return render(request, "view_question.html", {"deck": deck})

@login_required
def view_answer(request,pk):
    deck = get_object_or_404(request.user.decks, pk=pk)
    return render(request, "view_answer.html", {"deck": deck})
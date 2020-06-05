from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Deck 
from .forms import DeckForm

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
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
    card_form = CardForm()
    next_card = deck.cards.first()
    return render(request, "deck_detail.html", {"deck": deck, "card_form": card_form, "next_card": next_card})

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
def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method == "POST":
        form = CardForm(instance=card, data=request.POST)
        if form.is_valid():
            card = form.save()
            return redirect(to='deck_detail', pk=card.deck.pk)
    else:
        form = CardForm(instance=card)

    return render(request, "edit_card.html", {
        "form": form,
        "card": card,
        })

@login_required
def delete_deck(request, pk):
    deck = get_object_or_404(request.user.decks, pk=pk)
    if request.method == "POST":
        deck.delete()
        return redirect(to='deck_list')

    return render(request, "delete_deck.html", {"deck": deck})   

@login_required
def view_question(request,card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    
    return render(request, "view_question.html", {"card": card, "deck": card.deck,})

@login_required
def next_question(request,card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    next_pk = card.deck.cards.order_by('?').first().pk
    
    return redirect('view_question', card_pk=next_pk)


@login_required
def next_card(request,card_pk):
    card = get_object_or_404(Card, pk=card_pk)

    return render(request, "next_question")
    



@login_required
def view_answer(request,card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    return render(request, "view_answer.html", {"card": card, "deck": card.deck,})

@login_required
def delete_flashcard(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)

    if request.method == "POST":
        card.delete()
        return redirect (to='deck_detail')
    
    return render(request, "delete_flashcard.html", {"card": card, "deck": card.deck,})

# @login_required
# def view_tag(request, tag_name):
#     tag = get_object_or_404(Tag, tag=tag_name)
    

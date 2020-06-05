from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Deck #or Flashcards

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='deck_list')

    return render (request, "home.html")

@login_required
def deck_list(request):    
    decks = request.user.decks.all()

    return render(request, 'deck_list.html', {"decks": decks})

# @login_required
# def flashcards_detail(request,pk):
#     flashcards = get_object_or_404(request.user.flashcards, pk=pk)
#     return render(request, "flashcards")

# @login_required
# def add_card(request, deck_pk):
#     deck = get_object_or_404(request.user.deck, pk=deck_pk)

#     if request.method == "POST": #submitted the form
#         form = FlashcardForm(data=request.POST)
#         if form.is_valid():
#             flashcard = form.save(commit=False)
#             flashcard.deck = deck
#             flashcard.save()
#             return redirect(to='deck_list', deck_pk=deck.pk)
#     else: #viewing page for the first time
#         form = FlashcardForm()

#     return render(request, "deck/add_card.html", {
#            
# 
# })    
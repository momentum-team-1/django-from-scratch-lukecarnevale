from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import FlashcardsForm

def homepage(request):
    if request.user.is_authenticated():
        return redirect(to='flashcards')
        
    return render (request, "flashcards/home.html")

@login_required
def flashcards_list(request):    
    your_flashcards = request.user.flashcards.all()

    return render(request, 'flashcards/home.html', {"flashcards": your_flashcards})

@login_required
def flashcards_detail(request,pk):
    flashcards = get_object_or_404(request.user.flashcards, pk=pk)
    return render(request, "flashcards")
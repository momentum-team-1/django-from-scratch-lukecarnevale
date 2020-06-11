"""flashcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from cards import views as flashcards_views

urlpatterns = [
    path('', flashcards_views.homepage, name="homepage"),
    path('flashcards/', flashcards_views.deck_list, name='deck_list'),
    path('flashcards/<int:pk>/', flashcards_views.deck_detail, name='deck_detail'),
    path('flashcards/<int:pk>/edit/', flashcards_views.edit_card, name='edit_card'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('new/', flashcards_views.add_deck, name='add_deck'),
    path('flashcards/<int:pk>/add_card/', flashcards_views.add_card, name='add_card'),
    path('flashcards/<int:pk>/delete/', flashcards_views.delete_deck, name='delete_deck'),
    path('flashcards/<int:card_pk>/view_question/', flashcards_views.view_question, name='view_question'),
    path('flashcards/<int:card_pk>/delete_flashcard/', flashcards_views.delete_flashcard, name='delete_flashcard'),
    path('flashcards/<int:card_pk>/next_question/', flashcards_views.next_question, name='next_question'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

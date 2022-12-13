from django.urls import path

from .views.game_view import game_view
from .views.game_list_view import game_list_view
from .views.game_genre_view import game_genre_view
from .views.game_genre_list_view import game_genre_list_view


urlpatterns = [
    path('<int:id>', game_view, name='game_view'),
    path('list', game_list_view, name='game_list'),
    path('genre/<int:id>', game_genre_view, name='game_genre'),
    path('genre/list', game_genre_list_view, name='game_genre_list'),
]
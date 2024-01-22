from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players, name='players'),
    path('players/test/', views.test, name='test'),
    path('players/scout/', views.scout, name='scout')
]
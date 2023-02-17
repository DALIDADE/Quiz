from django.urls import path
from .views import *


urlpatterns = [
    path('',Login,name='login-page'),
    path('mugallym',Mugallym,name = 'mugallym-page'),
    path('duzedis',DuzedisView,name = 'duzedis-page'),
    path('testmaglumatlary',TestMaglumatlaryView,name='testmaglumatlary-page'),
    path('testgosmak',TestGosmakView,name='testgosmak-page'),
    path('statistika',StatistikaView,name = 'statistika-page'),
    path('netijeler',NetijelerView,name = 'netijeler-page'),
    path('testpozmak',TestPozmakView,name = 'tetpozmak-page'),
    path('testuytgetmek',Testuytgetmek,name = 'testuytgetmek-page'),
    path('uytget/<int:id>',UytgetView,name = 'uytget-page')
]
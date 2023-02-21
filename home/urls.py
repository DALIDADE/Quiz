from django.urls import path
from .views import *


urlpatterns = [
    path('',Login,name='login-page'),
    path('mugallym',Mugallym,name = 'mugallym-page'),
    # path('duzedis',DuzedisView,name = 'duzedis-page'),
    path('testmaglumatlary',TestMaglumatlaryView,name='testmaglumatlary-page'),
    path('testgosmak',TestGosmakView,name='testgosmak-page'),
    path('statistika',StatistikaView,name = 'statistika-page'),
    path('testpozmak',TestPozmakView,name = 'tetpozmak-page'),
    path('maglumat',MaglumatView,name = 'maglumat-page'),
    path('testuytgetmek/<int:id>',TestUytgetmekView,name= 'testuytgetmek-page'),
    # path('testuytgetmek',Testuytgetmek,name = 'testuytgetmek-page'),
    path('uytget/<int:id>',UytgetView,name = 'uytget-page'),
    path('logout',Logout,name='logout-page'),

]
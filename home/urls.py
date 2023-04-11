from django.urls import path
from .views import *



urlpatterns = [
    path('',Login,name='login-page'),
    path('mugallym/<int:id>',Mugallym,name = 'mugallym-page'),
    path('testmaglumatlary<int:id>',TestMaglumatlaryView,name='testmaglumatlary-page'),
    path('testgosmak/<str:at>/<int:pk>/<int:id>',TestGosmakView,name='testgosmak-page'),
    path('statistika/<str:at>',StatistikaView,name = 'statistika-page'),
    path('testpozmak/<int:id>',TestPozmakView,name = 'tetpozmak-page'),
    path('maglumat/<int:id>',MaglumatView,name = 'maglumat-page'),
    path('testuytgetmek/<int:id>',TestUytgetmekView,name= 'testuytgetmek-page'),
    path('testuytgetmek2/<str:at>',TestUytgetmek2View,name= 'testuytgetmek2-page'),
    path('logout/',Logout,name='logout-page'),

]
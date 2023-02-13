from django.urls import path
from .views import*


urlpatterns = [
    path('',Login,name='login-page'),
    path('create',Create,name='create-page'),
    path('mugallym',Mugallym,name = 'mugallym-page'),
    path('testmaglumatlary/<str:pk>/',TestMaglumatlaryView,name='testmaglumatlary-page'),
    path('testgosmak/<str:pk>/',TestGosmakView,name='testgosmak-page'),
]

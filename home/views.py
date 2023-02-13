from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

def Create(request):
    Sapak = Sapaklar.objects.all()
    Fakulted = Fakultedlar.objects.all()
    Topor = Toporlar.objects.all()

    context = {
    'Sapak':Sapak,
    'Fakulted':Fakulted,
    'Topor':Topor
}
    return render(request,'create.html',context)



def Mugallym(request):

    Sapak = Sapaklar.objects.all()
    Fakulted = Fakultedlar.objects.all()
    Topar = Toparlar.objects.all()
    context = {
        'Sapak':Sapak,
        'Fakulted':Fakulted,
        'Topar':Topar
    }
    return render (request,'mugallym.html',context)




def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('mugallym-page')
          
        else:
            messages.info(request,'Username or password is incorrect')
        
    return render(request,'login.html')



def TestMaglumatlaryView(request,pk):
    form =TestMaglumatlaryForm()
    if request.method == "POST":
        form = TestMaglumatlaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testmaglumatlary-page',pk)

    context = {
        'form' :form
    }
    return render(request,'testmaglumatlary.html',context)



def TestGosmakView(request,pk):
    form = TestGosmakForm()
    if request.method == "POST":
        form = TestGosmakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testgosmak-page',pk)
    context = {
        'form':form
    }
    return render (request,'testgosmak.html',context)



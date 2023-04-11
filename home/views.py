from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from student.models import Netijeler
from .models import *
from .forms import *







def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(request,username=username,password=password)
        except:
            messages.error(request, 'User girizilmedi')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if len(username) == 6:
                return redirect('homestudent-page',id=user.id)
            else:
                return redirect ('mugallym-page',id=user.id)
        else:
            return redirect('login-page')
    return render(request,'login.html')




@login_required(login_url='')
def Mugallym(request,id):
    user = User.objects.get(id=request.user.id)
    Maglumatlar = TestMaglumatlary.objects.filter(user=user)
    context = {
        'Maglumatlar':Maglumatlar,
    }
    return render (request,'mugallym.html',context)





def MaglumatView(request,id):
    user = User.objects.get(id=request.user.id)
    Maglumatlar = TestMaglumatlary.objects.filter(user=request.user)
    context = {
        'Maglumatlar':Maglumatlar,
    }
    return render(request,'maglumat.html',context)




@login_required(login_url='')
def TestMaglumatlaryView(request,id):
    user = User.objects.get(id=request.user.id)
    form = TestMaglumatlaryForm()
    if request.method == "POST":
        user = request.user
        form = TestMaglumatlaryForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('testgosmak-page',at=order.Testin_ady,pk=order.Sorag_sany,id=user.id)
    context = {
        'form' :form,
    }
    return render(request,'testmaglumatlary.html',context)









@login_required(login_url='')
def TestGosmakView(request,at,pk,id):
    property1=TestMaglumatlary.objects.get(Testin_ady=at)
    form = TestGosmakForm()
    if pk>0:
        if request.method == "POST":
            form = TestGosmakForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.property = property1
                comment.save()
                pk=pk-1
                return redirect('testgosmak-page',at=property1,pk=pk,id=id)
    else:
        return redirect('mugallym-page',id=id)
    context = {
        'pk':pk,
        'id':id,
        'property1':property1,
        'form':form,
    }
    return render (request,'testgosmak.html',context)






@login_required(login_url='')
def TestUytgetmekView(request,id):
    testler = TestGosmak.objects.filter(property=id)
    context = {
        'testler':testler
    }
    return render (request,'testuytgetmek.html',context)





@login_required(login_url='')
def TestUytgetmek2View(request,at):
    testler = TestGosmak.objects.filter(Soragy=at)
    context = {
        'testler':testler
    }
    if request.method == 'POST':
        testler = TestGosmak.objects.filter(Soragy=at)
        for i in testler:
            i.Soragy = request.POST['w1']
            i.a = request.POST['w2']
            i.b = request.POST['w3']
            i.c = request.POST['w4']
            i.save()
            return redirect('maglumat-page' ,request.user.id)
    return render (request,'testuytgetmek2.html',context)



@login_required(login_url='')
def StatistikaView(request,at):
    Netije = Netijeler.objects.filter(Testin_ady=at)
    print(Netije)
    context = {
        'Netije':Netije
    }
    return render (request,'statistika.html',context)




@login_required(login_url='')
def TestPozmakView(request,id):
    user = User.objects.get(id=request.user.id)
    Maglumatlar = TestMaglumatlary.objects.filter(id=id)
    if request.method == 'POST':
        Maglumatlar.delete()
        return redirect('maglumat-page' ,user.id)
    context = {
        'Maglumatlar':Maglumatlar
    }
    return render(request,'testpozmak.html',context )







@login_required(login_url='')
def Logout(request):
    logout(request)
    return redirect('login-page')








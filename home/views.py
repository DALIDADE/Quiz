from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# def Create(request):
#     Sapak = Sapaklar.objects.all()
#     Fakulted = Fakultedlar.objects.all()
#     Topor = Toporlar.objects.all()

#     context = {
#     'Sapak':Sapak,
#     'Fakulted':Fakulted,
#     'Topor':Topor
# }
#     return render(request,'create.html',context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
     
        # try:
        #     user = User.objects.get(request,username=username,password=password)
        
        # except:
        #     messages.error(request, 'User girizilmedi')
        user = authenticate(request, username=username, password=password)
        print('Birinji')
        if user is not None:
            login(request, user)
            print('IF')
            return redirect ('mugallym-page')
            
    
        else:
            return redirect('login-page')
            
            
            
        
    return render(request,'login.html')

def Mugallym(request):
    Sapak = Sapaklar.objects.all()
    # Topar = Toparlar.objects.all()
    Maglumatlar = TestMaglumatlary.objects.all()
    context = {
        'Maglumatlar':Maglumatlar,
    }
    return render (request,'mugallym.html',context)



# def DuzedisView(request):
#     Maglumatlar2 = TestMaglumatlary.objects.all()
#     context = {
#         'Maglumatlar2':Maglumatlar2
#     }
#     return render (request,'duzedis.html', context)





def TestMaglumatlaryView(request):
    form = TestMaglumatlaryForm()
    if request.method == "POST":
        form = TestMaglumatlaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testgosmak-page')
    context = {
        'form' :form,
    }
    return render(request,'testmaglumatlary.html',context)





def TestGosmakView(request):
    form = TestGosmakForm()
    if request.method == "POST":
        form = TestGosmakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testgosmak-page')
    context = {
        'form':form
    }
    return render (request,'testgosmak.html',context)


# def Testuytgetmek(request):
#     tazeler = TestMaglumatlary.objects.all()

#     context = {
#         'tazeler':tazeler
#     }
#     return render (request,'testuytgetmek.html',context)

def UytgetView(request,id):
    duzedisler = TestMaglumatlary.objects.get(id=id)
    if request.method == 'POST':
        duzedisler.Sapagyn_ady=Sapaklar.objects.get(Sapagyn_ady=request.POST['u1'])
        duzedisler.Testin_ady=request.POST['u2']
        duzedisler.Topar=Toparlar.objects.get(Topar=request.POST['u3'])
        duzedisler.Sorag_sany=request.POST['u4']
        duzedisler.Wagyt_limidi=request.POST['u5']
        
        duzedisler.save()
        print('boldy')
    context = {
        'duzedisler':duzedisler
    }
    return render(request,'uytget.html',context)

def TestUytgetmekView(request,id):
    testler = TestGosmak.objects.get(id=id)
    if request.method=='POST':
        testler.Soragy = request.POST['w1']
        testler.a = request.POST['w2']
        testler.b = request.POST['w3']
        testler.c = request.POST['w4']
        testler.d = request.POST['w5']
        testler.save()

        print('Yatda sakladym')
    context = {
        'testler':testler
    }
    return render (request,'testuytgetmek.html',context)

def Logout(request):
    logout(request)
    return redirect('mugallym-page')

def StatistikaView(request):
    return render (request,'statistika.html')


def TestPozmakView(request):
    return render(request,'testpozmak.html')

def MaglumatView(request):
    Maglumatlar = TestMaglumatlary.objects.all()
    context = {
        'Maglumatlar':Maglumatlar,
    }
    return render(request,'maglumat.html',context)

    



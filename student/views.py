from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from home.views import *
from .forms import*


@login_required(login_url='')
def HomeStudentView(request,id):
    user1 = Student.objects.filter(user=request.user)
    for i in user1:
        b=i.topar
    Maglumatlar = TestMaglumatlary.objects.filter(Topar=b)
    context = {
        'Maglumatlar':Maglumatlar
    }
    return render(request,'homestudent.html',context)


@login_required(login_url='')
def TestView(request,id):
    print(id)
    TestMaglumaty = TestGosmak.objects.filter(property=id)
    TestMaglumaty2 = TestMaglumatlary.objects.filter(id=id)
    j=0
    v=0
    x=0 
    a=[]
    for i in  TestMaglumaty:
        a.append(i)
    b=[a[j]]
    k=j+1
    context = {
        'TestMaglumaty2':TestMaglumaty2,
        'TestMaglumaty':TestMaglumaty,
        'p':b,
        'j':j,
        'id':id,
        'k':k,
        'v':v,
        'x':x
    }
    return render (request,'test.html',context)


@login_required(login_url='')
def Test2(request,pk,id,v,x): 
    if request.method=='POST':
        TestMaglumaty = TestGosmak.objects.filter(property=id)
        TestMaglumaty2 = TestMaglumatlary.objects.filter(id=id)
        print('testmaglumaty=',TestMaglumaty2)
        j=pk
        print("v=",v)
        print('x=',x)
        print(j)
        print('id=',id)
        a=[]
        l=[]
        x=x+1
        for i in TestMaglumaty:
            a.append(i)
        b=[a[j]]
        d=request.POST.get('a')
        q=request.POST.get('b')
        w=request.POST.get('c')
        for m in b:
            if d==m.dogry:
                v=v+1
                print('dogry=',d)
                break
            if q==m.dogry:
                v=v+1
                print('dogry=',q)
                break
            if w==m.dogry:
                v=v+1
                print('dogry=',w)
                break
        print('dogry sany=',v)
        print('yalnys sany=',x-v)
        print('sorag sany=',x)
        c=len(a)
        if c-1>j:
            print('ISLEYA')
            j=j+1 
            k=j+1
            b=[a[j]]
            print(b)
            context={
                'p':b,
                'j':j,
                'id':id,
                'k':k,
                'x':x,
                'v':v,
                'TestMaglumaty2':TestMaglumaty2,
            }
            return render(request,'test.html',context)
        else:
            for i in TestMaglumaty2:
                topary = i.Topar
                Dersin_ady = i.Sapagyn_ady
                Testin_ady = i.Testin_ady
                context2={
                    'j':j,
                    'x':x,
                    'v':v,
                    'topary':topary,
                    'Dersin_ady':Dersin_ady,
                    'Testin_ady':Testin_ady
                }
                return render(request,'test_sony.html',context2)
    else:
        return HttpResponse('nadory yer')

def TestSonyView(request,j,x,v,topary,Dersin_ady,Testin_ady):
    print('j=',j)
    print('x=',x)
    print('v=',v)
    print('topary=',topary)
    print('Dersin_ady=',Dersin_ady)
    print('Testin_ady=',Testin_ady)
    context={ 
        'j':j,
        'x':x,
        'v':v,
        'topary':topary,
        'Dersin_ady':Dersin_ady,
        'Testin_ady':Testin_ady
     }
    return render(request,'test_sony.html')


@login_required(login_url='')      
def SaveView(request,j,x,v,topary,Dersin_ady,Testin_ady):
    if request.method=='POST':
        print('Dersin ady=', Dersin_ady)
        j=j
        Sorag_sany = x
        Yalnys_sany=x-v
        Dogry_sany=v
        topary=topary
        Dersin_ady=Dersin_ady
        Testin_ady = Testin_ady
        Bahasy = (100/Sorag_sany)*Dogry_sany
        print('Sorag sany=', Sorag_sany)
        print('Yalnys_sany=', Yalnys_sany)
        print('Dogry_sany=', Dogry_sany)
        print('topary=', topary)
        print('Dersin_ady=',Dersin_ady)
        print('testin_ady=',Testin_ady)
        print('bahasy=', Bahasy)

        
    
        q=Netijeler(Topar=Toparlar.objects.get(Topar=topary),
                                    Dersin_ady=Sapaklar.objects.get(Sapagyn_ady=Dersin_ady),
                                    Testin_ady=Testin_ady,
                                    user=request.user,
                                    Sorag_sany= Sorag_sany,
                                    Dogry_sany=Dogry_sany,
                                    Yalnys_sany=Yalnys_sany,
                                    Bahasy = Bahasy) 
        q.save()
        print('yatda saklandy netijeler')
        return redirect('netije2-page',Testin_ady)
    else:
        return HttpResponse('ASIPKA')


@login_required(login_url='')
def  NetijeView(request):
    Netije = Netijeler.objects.filter(user=request.user.id)
    context={
        'Netije':Netije
    }
    return render(request,'netije.html',context)


@login_required(login_url='')
def  Netije2View(request,Testin_ady):
    Netije = Netijeler.objects.filter(user=request.user.id ,Testin_ady=Testin_ady)
    context={
        'Netije':Netije
    }
    return render(request,'netije2.html',context)



@login_required(login_url='')
def Logout(request):
    logout(request)
    return redirect('login-page')
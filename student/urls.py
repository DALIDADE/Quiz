from django.urls import path,include
from .views import *



urlpatterns = [
    path('save/<int:j>/<int:x>/<int:v>/<str:topary>/<str:Dersin_ady>/<str:Testin_ady>',
                                                                SaveView,name='save-page'),
    path('homestudent<int:id>',
                            HomeStudentView , name = 'homestudent-page'),
    path('test2/<int:pk>/<int:id><int:v>/<int:x>',
                                                Test2,name='test2-page'),
    path('test/<int:id>/',
                        TestView,name = 'test-page'),
    path('test_sony/<int:j>/<int:x>/<int:v>/<str:topary>/<str:Dersin_ady>/<str:Testin_ady>',
                                                                    TestSonyView, name = 'testsony-page'),
    path('netije',NetijeView,name='netije-page'),
    path('netije2/<str:Testin_ady>',Netije2View,name='netije2-page')

]
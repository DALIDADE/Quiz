from django.db import models
from home.models import Sapaklar,Toparlar
from django.contrib.auth.models import User 

class Netijeler(models.Model):
    Topar = models.ForeignKey(Toparlar, on_delete=models.CASCADE,null=True)
    Dersin_ady = models.ForeignKey(Sapaklar, on_delete=models.CASCADE,null=True)
    Testin_ady = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    Sorag_sany = models.SmallIntegerField(null=True,blank=True)
    Dogry_sany = models.SmallIntegerField(null=True,blank=True)
    Yalnys_sany = models.SmallIntegerField(null=True,blank=True)
    Bahasy = models.SmallIntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.Topar)    

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topar = models.ForeignKey(Toparlar, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.topar)

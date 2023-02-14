from django.db import models

class Fakultedlar(models.Model):
    Fakultedin_ady = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Fakultedin_ady

class Sapaklar(models.Model):
    Sapagyn_ady = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Sapagyn_ady

class Toparlar(models.Model):
    Topar = models.PositiveIntegerField()

class TestMaglumatlary(models.Model):
    Fakultedin_ady = models.ForeignKey(Fakultedlar, on_delete= models.CASCADE)
    Sapagyn_ady = models.ForeignKey(Sapaklar, on_delete = models.CASCADE)
    Testin_ady = models.CharField(max_length=255)
    Topar = models.ForeignKey(Toparlar, on_delete = models.CASCADE)
    Sorag_sany = models.PositiveIntegerField()
    Wagyt_limidi = models.PositiveIntegerField()

    def __str__(self):
        return self.Testin_ady

class TestGosmak(models.Model):
    Soragy = models.TextField()
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d= models.CharField(max_length=100)








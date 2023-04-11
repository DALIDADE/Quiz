from django.contrib import admin
from .models import *

class Liboy(admin.StackedInline):
    model = TestGosmak

class Property(admin.ModelAdmin):
    inlines = [ Liboy ]
    class Meta:
        model = TestMaglumatlary

admin.site.register(TestMaglumatlary,Property)
admin.site.register(Sapaklar)
admin.site.register(Toparlar)




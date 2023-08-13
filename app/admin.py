from django.contrib import admin
from .models import appmodel,Article


class appAdmin(admin.ModelAdmin):
    list=['name','fathername','number','address','join']

admin.site.register(appmodel,appAdmin)

class art_adming(admin.ModelAdmin):
    list_display=["date",'litre','rate','name']
admin.site.register(Article,art_adming)

# Register your models here.

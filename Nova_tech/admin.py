from django.contrib import admin
from .models import *
# Register your models here.
class Serviceadmin(admin.ModelAdmin):
    list_display = ('title','content','image')
    search_fields = ['title',]

admin.site.register(Service,Serviceadmin)

ets='Novatech'
admin.site.site_title=ets
admin.site.site_header=ets
admin.site.index_title=ets

#admin: knjsoft; mdp:admin
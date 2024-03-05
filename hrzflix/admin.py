from django.contrib import admin
from .models import *

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','genre','theme','duration','rating']

class SliderAdmin(admin.ModelAdmin):
    list_display=['name','duration','rating','description']
    
admin.site.register(Genre)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Movie,MovieAdmin)



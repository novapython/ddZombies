from crossstitch.models import Patterns, Zombies
from django.contrib import admin

class ZombieAdmin(admin.ModelAdmin):
	fields = ['name', 'rotdegree', 'favorite']

class PatternAdmin(admin.ModelAdmin):
	fields = ['name', 'count', 'grid', 'image']

admin.site.register(Patterns, PatternAdmin)
admin.site.register(Zombies, ZombieAdmin)

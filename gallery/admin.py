from django.contrib import admin

# Register your models here.
from .models import Album,Photo

class ChoiceInline(admin.TabularInline):
    model=Photo
    extra=1


class AlbumAdmin(admin.ModelAdmin):
	inlines=[ChoiceInline]
	list_display = ('album_name','desc')
	

admin.site.register(Album, AlbumAdmin)


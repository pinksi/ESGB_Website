from django.contrib import admin

# Register your models here.
from .models import Types
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ["__str__","types","name","post","dept"]

class TypesAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
#	list_display = ["title","updated", "timestamp"]
#	list_editable = ["title"]
#	list_display_links = ["updated"]
#	list_filter = ["updated", "timestamp"]
#	search_fields = ["title", "content"]
#	class Meta:
#		model = Post

admin.site.register(Post)#, PostModelAdmin)
admin.site.register(Types)

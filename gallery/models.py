from django.db import models
from django.utils import timezone
# Create your models here.
class Album(models.Model):
	album_name= models.CharField(max_length=100,blank=False)
	desc = models.CharField(max_length=500, blank=False)

	def __str__(self):
		return self.album_name

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)	
    image = models.FileField(upload_to='uploads/', blank = True)
    name_text = models.CharField(max_length=20,blank=False)
    def __str__(self):
        return self.name_text
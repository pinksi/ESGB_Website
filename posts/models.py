from django.db import models

# Create your models here.
class Types(models.Model):
	types_title = models.CharField(max_length=100,default='None')

	def __str__(self):
		return self.types_title


class Post(models.Model):
 	#title = models.CharField(max_length=150)
	#content = models.TextField()
	#updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	#timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	types = models.ForeignKey(Types, on_delete=models.CASCADE)
	name = models.CharField(max_length=100,blank=False)
	post = models.CharField(max_length=100, blank=False)
	dept = models.CharField(max_length=100, blank=False)
	upload_image = models.FileField(upload_to='uploads/', blank = True)

	def __str__(self):
		return self.name



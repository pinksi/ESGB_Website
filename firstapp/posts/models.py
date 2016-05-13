from django.db import models

# Create your models here.
class Post(models.Model):
	#title = models.CharField(max_length=150)
	#content = models.TextField()
	#updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	#timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	name = models.CharField(max_length=100,blank=False)
	post = models.CharField(max_length=100, blank=False)
	dept = models.CharField(max_length=100, blank=False)
	upload_image = models.ImageField(upload_to='uploads/', blank = True)
#	def __unicode__(self):
#		return self.title

	def __str__(self):
		return self.name



from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	upload_photos = models.FileField(upload_to='uploads/', blank = True)

	def __str__(self):
		return self.title
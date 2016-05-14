from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):

	context = {
		"name" : "home"
	}
	return render(request, "home.html", context)
	#return HttpResponse("<h1>home page </h1>")

def aboutus(request):
	context = {
		"aboutus" : "About Us"
	}
	return render(request, "aboutus.html",context)

def committe(request):
	post = Post.objects.all()
	context = {
		'post' : post
	}
	return render(request, "committe.html",context)
	

def login(request):
	if request.user.is_authenticated():
		context = {
			"title" : "My user"
		}
	else:
		context = {
			"title" : "Not authenticated"
		}
	return render(request, "index.html", context)

#def post_delete(request):
#	return HttpResponse("<h1>delete</h1>")



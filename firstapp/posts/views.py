from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "index.html", {})
	#return HttpResponse("<h1>home page </h1>")

def aboutus(request):
	return HttpResponse("<h1>details abt esgb</h1>")

def members(request):
	return HttpResponse("<h1>list of members</h1>")

def login(request):
	return HttpResponse("<h1>login</h1>")

#def post_delete(request):
#	return HttpResponse("<h1>delete</h1>")



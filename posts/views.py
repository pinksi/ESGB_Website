from django.http import HttpResponse
from django.shortcuts import render
from .models import Types
from .models import Post
from django.db.models import Q

# Create your views here.
def home(request):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		context = {
			"name" : "home"
		}
	return render(request, "home.html", context)
	#return HttpResponse("<h1>home page </h1>")

def aboutus(request):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		context = {
			"title" : "aboutus"
		}
	return render(request, "aboutus.html",context)

def committe(request):
	c = Types.objects.get(pk = 1)
	queryset1= c.post_set.all()
	c = Types.objects.get(pk = 2)
	queryset2= c.post_set.all()
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		context = {
			'query1' : queryset1,
			#'query1' : q
			'query2' : queryset2
		}
	return render(request, "committe.html",context)
	
def activity(request):
	query = request.GET.get("query")
	if query:
		srch = search(request, query)
		return srch
	else:
		context = {
			"activity" : "activity"
		}
	return render(request, "activity.html", context)

def login(request):
	if request.user.is_authenticated():
		context = {
			"title" : "My user"
		}
	else:
		context = {
			"title" : "not authenticated"
		}
	return render(request, "index.html", context)

#def post_delete(request):
#	return HttpResponse("<h1>delete</h1>")



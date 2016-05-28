from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog

# Create your views here.
def blogpost(request):
	blog_list = Blog.objects.all()
	paginator = Paginator(blog_list, 3)
	page = request.GET.get('page')
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	context = {
			'blog' : blogs
		}
	return render(request, "blog.html", context)
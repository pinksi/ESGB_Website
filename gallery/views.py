from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Album,Photo

# Create your views here.
class GalleryView(generic.DetailView):
    template_name = 'gallery.html'
    model=Album

    def get_queryset(self):
        return Album.objects.all()
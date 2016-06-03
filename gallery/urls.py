from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', views.GalleryView.as_view(), name='gallery'),
    ]
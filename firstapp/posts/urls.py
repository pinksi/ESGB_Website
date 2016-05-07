from django.conf.urls import url
from django.contrib import admin

from .views import (
	home,
	aboutus,
	members,
	login,
	)

urlpatterns = [
	url(r'^$', home),
    url(r'^aboutus/$', aboutus),
    url(r'^members/$', members),
    url(r'^login/$', login),
    
    #url(r'^posts/$', "<appname>.views.<function_name>"),  
]

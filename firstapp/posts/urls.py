from django.conf.urls import url
from django.contrib import admin

from .import views
#(
#	home,
#	aboutus,
#	committe,
#	login,
#	)

urlpatterns = [
	url(r'^$', views.home, name="home"),
    url(r'^aboutus/$', views.aboutus, name="aboutus"),
    url(r'^committe/$', views.committe,name="committe"),
    url(r'^login/$', views.login, name="login"),
    
    #url(r'^posts/$', "<appname>.views.<function_name>"),  
]

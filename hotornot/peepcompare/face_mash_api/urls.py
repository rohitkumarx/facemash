from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import (
	FaceMashListApiView, 
	FMDetailApiView,
	FaceMashUpdateApiView,
	FaceMashDeleteApiView,
	FaceMashCreateApiView
)


urlpatterns = [
    
    url(r'^$',FaceMashListApiView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', FMDetailApiView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', FaceMashUpdateApiView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', FaceMashDeleteApiView.as_view(), name='delete'),
    url(r'^create/$', FaceMashCreateApiView.as_view(), name='create'),


]
# Comic book fans of Reddit, what would you have done differently, if you have given a chance to jumpstart DC Extended Universe in the light of recent Marvel success. (Only condintion is, it have to be in 4 movies with same titles)? 

# What stories have you chosen? What character you have introduced in a movie. Like, I think grren lantern
# can be introduced in  

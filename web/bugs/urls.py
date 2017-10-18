from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$', views.home),
	url(r'project/([0-9]+)/$', views.project)
]

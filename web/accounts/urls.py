from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm

login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/bugs')

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login_forbidden(login), {'template_name': 'accounts/login.html', 'authentication_form': LoginForm}),
	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html', 'next_page': '/accounts/'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^register/complete/$', views.registration_complete, name='registration_complete'),
	url(r'^profile/$', views.profile, name='profile')
]

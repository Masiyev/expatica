# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate

@login_required
def home(request):
	numbers = [1,2,3,4,5]
	name = 'Max Rasul'
	args = {'name': name, 'numbers': numbers}
	return render(request, 'accounts/home.html', args)

@user_passes_test(lambda user: not user.username, redirect_field_name=None)
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(home)
		else:
			return render(request, 'accounts/reg_form.html', {'form': form})
	else:
		form = RegistrationForm()
		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def registration_complete(request):
	return render(request, 'accounts/registration_complete.html')

@login_required
def profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html', args)

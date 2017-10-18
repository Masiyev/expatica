# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import BugForm
from .models import Bug, Project

@login_required
def home(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bugs/index.html', {'projs': Project.objects.all()})
        else:
            return render(request, 'bugs/index.html', {'form': form})
    else:
        form = BugForm()
    return render(request, 'bugs/index.html', {'projs': Project.objects.all()})

@login_required
def project(request, nid = None):
    if nid == None:
        return redirect(home)
    else:
        result = Project.objects.filter(id=nid)
        if result:
            return render(request, 'bugs/project.html', {'proj': result[0]})
    return redirect(home)

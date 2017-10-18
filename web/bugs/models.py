# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

class Bug(models.Model):
    pid = models.ForeignKey(Project, on_delete=models.CASCADE, default=-1)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default='')

    def __str__(self):
        return "%s\n%s" % (self.name, self.description)

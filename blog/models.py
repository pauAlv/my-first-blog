#estas dos lineas son recursos que nos provee la carpeta de djangogirls
from django.db import models
from django.utils import timezone

class Post(models.Model): 
	#propiedades del objeto
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	#funciones del objeto
	def publish(self): #esto publica el objeto
		self.published_date = timezone.now()
		self.save()
	def __str__(self): #esto te regresa el titulo 
		return self.title


		"""
esto de arriba es esto:
Post
--------
title
text
author
created_date
published_date
		"""
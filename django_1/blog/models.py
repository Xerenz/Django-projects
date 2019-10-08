from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

'''Each class is a table
Each variable declared inside
is a field.

Django uses Object-Relation Mapping
to create an Object Orienetd Relational
DB like experience.'''

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

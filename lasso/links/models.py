from django.db import models


class Link(models.Model):
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Tag(models.Model):
	value = models.CharField(max_length=200)
	link = models.ForeignKey(Link)
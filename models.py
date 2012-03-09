from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

import random

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    #quote = models.ForeignKey(Quote, blank=True, null=True)
    owner = models.ForeignKey(User)
    slug = models.SlugField('slug')

    def __unicode__(self):
        return '%s by %s' %(self.name, self.owner.username)

    @models.permalink
    def get_absolute_url(self):
        return ('book', (), {
            'user': self.owner.username,
            'slug':self.slug})

class RandomQuotesManager(models.Manager):
    def random_quotes(self):
        i = 0
        quotes = []
        while (i < 7):
            quotes.append(self.all()[random.randrange(0,self.all().count() -1 )])
            i = i + 1
        return quotes

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    book = models.ForeignKey(Book)
    slug = models.SlugField('slug')
    objects = RandomQuotesManager()

    def __unicode__(self):
        return '\"%s\" - %s' %(self.text, self.author)

    def seven_random_quotes(self):
        all = Quote.objects.all()
        i = 0
        while (i < 5):
            quotes.append(all[random.randrange(0,7)])
            i = i + 1
        return quotes

#    @models.permalink
#    def get_absolute_url(self):
#        return ('book')



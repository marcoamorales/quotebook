from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

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

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    book = models.ForeignKey(Book)
    slug = models.SlugField('slug')

    def __unicode__(self):
        return '\"%s\" - %s' %(self.text, self.author)

#    @models.permalink
#    def get_absolute_url(self):
#        return ('book')



# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from quotebook.models import *
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from quotebook.forms import *

def quotes(request):
    r_quotes = Quote.objects.random_quotes()
    context = {'r_quotes': r_quotes}
    return render_to_response('quotebook.html', RequestContext(request, context))

@login_required
def user_quotebooks(request, user):
    current_user = User.objects.get(username=user)
    quotebooks = Book.objects.filter(owner=current_user)
    context = {'quotebooks': quotebooks, 'theuser': user}
    return render_to_response('quotebook.html', RequestContext(request, context))

@login_required
def book(request, user, slug):
    book = Book.objects.get(slug=slug)
    context = {'book': book, 'theuser': user, "slug": slug}
    return render_to_response('book.html', RequestContext(request, context))

@login_required
def add_book(request):

    return render_to_response('book.html', RequestContext(request, context))

@login_required
def add_quote(request, user, slug):
    if request.method == 'POST':
        form = QuoteForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('book', user=request.user, slug=slug)
    else:
        form = QuoteForm(user=request.user)
        context = {'form': form, 'slug': slug}
    return render_to_response('add_quote.html', RequestContext(request, context))
__author__ = 'marco'

from django import forms
from django.forms import ModelForm
from quotebook.models import Book, Quote

#class BookForm(forms.Form):
#    name = forms.CharField(max_length=100)
#    description = forms.CharField(widget=forms.Textarea)
#
#class QuoteForm(forms.Form):
#    text = forms.CharField(widget=forms.Textarea)
#    author = forms.CharField(max_length=100)
#    source = forms.CharField(max_length=100)
#    book = forms.ModelChoiceField(queryset=Book.objects.none())
#
#    def __init__(self, user, *args, **kwargs):
#        super(QuoteForm, self).__init__(*args, **kwargs)
#        self.fields['book'].queryset = Book.objects.filter(owner=user)

class BookForm(ModelForm):
    class Meta:
        model = Book

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        exclude = ('slug')

    def __init__(self, user, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(owner=user)
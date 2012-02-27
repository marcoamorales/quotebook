from django.contrib import admin
from quotebook.models import *

class QuoteInLine(admin.TabularInline):
    model = Quote

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'description', 'owner',)
    prepopulated_fields = {
        'slug': ('name',),
        }
    inlines = [
        QuoteInLine,
    ]

class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ('text', 'author', 'source',)
    prepopulated_fields = {
        'slug': ('text',),
        }

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Book, BookAdmin)

from django.contrib import admin
from .models import Snippet

# Register your models here.
"""the highlighted field is automatically set by our custom save() method 
on the model, but the admin doesn't know this. It expects us to enter in 
a value here. To solve the problem update our admin.py file and set 
highlighted as a read-only field."""

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)

admin.site.register(Snippet)

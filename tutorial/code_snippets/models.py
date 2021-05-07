from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles




class Snippet(models.Model):
    LEXERS = [item for item in get_all_lexers() if item[1]]
    LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
    STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
    """auto_now_add sets the filed to current date and time"""
    created = models.DateTimeField(auto_now_add=True) 
    """blank=True, form validation will allow entry of an empty value."""
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()

    """ A sequence consisting itself of iterables of exactly two items 
    (e.g. [(A, B), (A, B) ...]) to use as choices for this field. If 
    choices are given, they’re enforced by model validation and the 
    default form widget will be a select box with these choices instead 
    of the standard text field. """
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments import highlight # new
from pygments.formatters.html import HtmlFormatter # new
from pygments.lexers import get_all_lexers, get_lexer_by_name # new



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

    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE) # new
    highlighted = models.TextField() # new

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs): # new
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

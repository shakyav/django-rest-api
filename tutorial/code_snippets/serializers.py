"""A Serializer transforms model instances into JSON"""

from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):

    """ takes the snippets model and transform all its attributes into json fileds"""

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos',
                  'language', 'style', )
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Snippet, STYLE_CHOICES, LANGUAGE_CHOICES

#class UserSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = User
        #fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['url','id', 'highlight', 'owner', 'title', 'code', 'lineos', 'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','id', 'username', 'snippets']
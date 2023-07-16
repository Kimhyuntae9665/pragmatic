from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget = forms.Textarea(attrs={'class':'editable',
                                                             'style':'height:auto; text-align:left ;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)
    class Meta:
        model = Article
        # witer는 보안상의 문제 때문에 제외 나중에 def form_valid로 추가할 것이다
        fields=['title','image','project','content']
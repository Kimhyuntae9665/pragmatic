from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # witer는 보안상의 문제 때문에 제외 나중에 def form_valid로 추가할 것이다
        fields=['title','image','content']
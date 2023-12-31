from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        # witer는 보안상의 문제 때문에 제외 나중에 def form_valid로 추가할 것이다
        fields=['image','title','description']
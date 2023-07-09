from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        #  fields 에 User 를 넣지 않은 이유는 field에 user 추가하면 user의 정보가 노출되면 보안 문제가 있어서
        fields = ['image','nickname','message']
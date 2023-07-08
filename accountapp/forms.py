from django.contrib.auth.forms import UserCreationForm
#                   UserCreationForm을 상속받는다
class AccountUpdateForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #  UserCreationForm 중에 username 필드를 비 활성화 한다
        self.fields['username'].disabled = True
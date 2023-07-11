from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'


    #  form_class에서 field에서 user를 추가하지 않았다 이유는 보안문제 때문에 하지만 이러면 페이지가 요구하는 사항을 만족하지 못한다
    #  그래서 VIew 논리를 구현하는 파일에서 user 필드도 추가해서 서버에 보내준다
    def form_valid(self, form):
        #  commit 데이터베이스에 저장하지는 않고 임시로 변수에 저장한다
        temp_profile = form.save(commit = False)
        #  user의 정보를 가져온다
        temp_profile.user = self.request.user
        #  form_class에 user의 정보를 더해서 데이터 베이스에 저장한다
        temp_profile.save()
        #  super인 조상 ProfileCreateView 여기에서 보내는 원래의 form_class 형태를 return 한다
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('accountapp:detail',kwargs={'pk':self.object.user.pk})




@method_decorator(profile_ownership_required,'get')
@method_decorator(profile_ownership_required,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'


    def get_success_url(self):
        #  deatil 페이지로 넘어갈려면 pk가 필요하다  kwargs : keywordsarguments 매개변수
        return reverse_lazy('accountapp:detail',kwargs={'pk':self.object.user.pk})
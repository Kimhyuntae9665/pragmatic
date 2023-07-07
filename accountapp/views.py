from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    # 여기는 서버가 request를 받았을때의 처리를 담당하는 곳
    #  서버가 request를 받았을때 render로 보여줄 페이지를 정하는 것
    if request.method == "POST":
        #      넘어온 request 요청에서 POST method를 사용해서 넘어온 요청에서 'hello_world_input'이라는 이름을 가진 데이터를 가져와라
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
    
        # reverse는 함수형 class 에서
        return  HttpResponseRedirect(reverse('accountapp:hello_world'))
    else :

        hello_world_list = HelloWorld.objects.all()
        return render(request,'accountapp/hello_world.html',context={'hello_world_list':hello_world_list})



#  class view 로 만든 class view
class AccountCreateView(CreateView):
    #  Django 에서 기본으로 제공해 주는 User model
    model = User
    #  User 를 만들때 Form 이 필요하다  ==> 나중에 create.html에서 {{form}}으로 적어서 UserCreationForm을 가져온다
    form_class = UserCreationForm
    # 성공했을 때 redirect 할 URL , reverse_lazy는 class형 view에서
    success_url = reverse_lazy('accountapp:hello_world')
    # 계정을 만들 때 사용할 template 파일의 이름
    template_name='accountapp/create.html'



class AccountDetailView(DetailView):
    # Detail View는 Read 이기때문에 model의 field 가 그리 많지 않다
    #  어떤 모델을 쓸지
    model = User
    # 어떤 파일로 어떻게 시각화 할지
    template_name= 'accountapp/detail.html'

    context_object_name='target_user'

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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
    

        return  HttpResponseRedirect(reverse('accountapp:hello_world'))
    else :

        hello_world_list = HelloWorld.objects.all()
        return render(request,'accountapp/hello_world.html',context={'hello_world_list':hello_world_list})




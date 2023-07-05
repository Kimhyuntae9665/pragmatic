from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    # 여기는 서버가 request를 받았을때의 처리를 담당하는 곳
    #  서버가 request를 받았을때 render로 보여줄 페이지를 정하는 것
    if request.method == "POST":
        return  render(request,'accountapp/hello_world.html',context={'text2':'POST METHOD!!!'})
    else :
        return render(request,'accountapp/hello_world.html',context={'text2':'GET METHOD!!!'})




"""
URL configuration for pragmatic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accountapp.urls')),
    path('profiles/',include('profileapp.urls')),
#     media에 관련한 추가적인 setting , pragmatic의 settings의 MEDIA_URL과 MEDIA_ROOT를 연결해서 서버에서 media 디렉토리에서 img파일을 가져온다
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

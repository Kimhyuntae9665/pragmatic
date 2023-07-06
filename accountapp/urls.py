from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name="accountapp"

urlpatterns = [
    path('hello_world/',hello_world,name='hello_world'),
    #                  class 형 view는 class이름.as_view()
    path('create/',AccountCreateView.as_view(),name='create')
]
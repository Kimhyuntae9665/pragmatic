from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name= 'profileapp'


urlpatterns = [
    path('create/',ProfileCreateView.as_view(),name='create'),
    #  어떤 profile에 접근해야 하는지 알아야 하니까 int:pk를 넣어야 한다 
    path('upadate/<int:pk>',ProfileUpdateView.as_view(),name='update'),
]
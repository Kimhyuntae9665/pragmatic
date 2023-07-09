from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # user field 는 이 class model의 주인을 정하는 것이다
    # User model과 연동하고 User 모델의 instance가 삭제되면 이 Profile instance도 자동 삭제
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    #  업로드한 이미지 파일을 서버 내부에 저장해야한다 저장할 경로를 정하는 것이 upload_to
    image = models.ImageField(upload_to='profile/',null=True)

    nickname =  models.CharField(max_length=20,unique=True,null=True)

    message = models.CharField(max_length=100,null=True)
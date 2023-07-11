from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    writer = models.ForeignKey(User,on_delete=models.SET_NULL, related_name='article',null=True)

    title = models.CharField(max_length=200,null=True)
    # CharField는 글자수를 명시해 줘야 하지만
    #  TextField는 글자 수 명시 안 해줘도 된다
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='article/',null=False)

    created_at = models.DateTimeField(auto_now_add=True,null=True)

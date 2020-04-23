from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#自定义用户模型类,因为美多商城多出了一个手机选项,所以要自定义添加一个并且继承AbstractUser
class User(AbstractUser):
    mobile=models.CharField(max_length=11)
    email_active = models.BooleanField(default=False)
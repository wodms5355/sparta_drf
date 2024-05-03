from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    birthday = models.DateTimeField("생일")
    gender_choice = (('M', '남성'), ('F', '여성'),)
    #성별을 선택할 수 있도록 따로 gender_choice라고 정의해두기!
    gender = models.CharField("성별", choices=gender_choice, blank=True, max_length=1)
    introduction = models.TextField("자기소개", blank=True)

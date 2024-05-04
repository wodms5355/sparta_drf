from django.db import models


# Create your models here.
class Product(models.Model):
    login_status = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(("이미지"), upload_to=None, height_field=None, width_field=None, max_length=None)
    #ImageField 및 upload_to를 사용하려면 media폴더를 만들어야함.
    #프로젝트 안에 media파일 생성
    #프로젝트 내의 settings.py에다가 MEDIA_ROOT와 MEDIA_URL을 설정
        #MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        #MEDIA_URL = '/media/'
    #
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.comments = None

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments"  #근데, CASCADE얜 뭘까
                                )  #이게 바로 역직렬화? 위에 사용된 Product class를 이용하는거자노,,,?
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

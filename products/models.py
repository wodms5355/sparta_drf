from django.db import models


# Create your models here.
class Product(models.Model):
    login_status = models.BooleanField(default=False)
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(("이미지"), upload_to=None, height_field=None, width_field=None, max_length=None)
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

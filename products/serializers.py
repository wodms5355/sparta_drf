from django.contrib.auth import get_product_model
from rest_framework import serializers
from products.models import Comment, Product

#Product = get_product_model
#Comment = get_comment_model


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("product",)
        #특정 필드를 직렬화 로직에 포함하지 않고 반환 값에만 필드(조건)를(을)) 포함하도록 하기 위해서 / 특정필드 = account

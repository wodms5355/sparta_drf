from django.urls import path
from. import views

app_name= "products"
urlpatterns = [
    path("", views.ProductListAPIView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
    path("<int:pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list", ),
    path("/comments/<int:comment_pk>/", views.CommentDetailAPIView.as_view(), name="comment_detail",

         ),
    # as_view()를 사용함으로써 class자체가 넘어오는(다고 이해하는게 맞나..?질문 해야겠다) 것이 아니라 호출 할수 있음!
]



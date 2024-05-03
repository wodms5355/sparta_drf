from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from. import views


app_name = "accounts"
urlpatterns = [

    path("", views.SignupAPIView.as_view(), name="signup"),
    #회원가입을 보여주는 url!

    # path("login/", views.LoginAPIView.as_view(), name="login"),
    # 이렇게 작성하고 signupAPIView에서 했던 것처럼 모든 내용을 작성해줘도 괜찮지만,
    path("login/", TokenObtainPairView.as_view(), name="login"),
    #TokenObtainPairView.as_view()는 DRF에서 제공하는 JWT를 얻기위한 메서드!!
    #TokenObtainPairView는 이름처럼 클래스 기반 뷰를 반환!
    # 이를 URL 패턴에 등록해 사용할 수도 있고, 주로 인증된 사용자가 로그인할 때 토큰을 얻는 데 사용된다!
    path("<str:username>/", views.UserDetailAPIView.as_view(), name="user_detail"),

    #path("json_profile/",views.json_profile,name="json_profile"),
]

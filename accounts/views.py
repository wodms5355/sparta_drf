#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from accounts.serializers import UserSerializer


#from django.http.response import JsonResponse
#from rest_framework.decorators import api_view
#from accounts.models import User
#from accounts.serializers import UserSerializer


class SignupAPIView(APIView):
    def post(self, request):  #새로 계정을 생성하는 거니까 http의 생성 메소드인 post사용
        data = request.data  #  post 요청으로 받아온 데이터를 의미
        email = data.get("email")  #요청받은 데이터에서 이메일 값을 가져와!
        username = data.get("username")  #요청받은 데이터에서 사용자이름 값을 가져와!
        #과제에서 email과 username은 유일해야한다고 했기 때문에 적은거임!

        if not (email and username):
            return Response({"error": "email or username required"}, status=400)
        #만약에 email과 username이 데이터에 없으면, {}안의 값을 반환 해줘

        if get_user_model().objects.filter(email=email).exists():
            return Response({"error": "email already exists"}, status=400)
        #email은 유일 해야 한다고 했기 때문에 이미 해당 내용이 존재 한다면, {}를 보여줘

        if get_user_model().objects.filter(username=username).exists():
            return Response({"error": "username already exists"}, status=400)
        # username도 유일 해야 한다고 했기 때문에 이미 해당 내용이 존재 한다면, {}를 보여줘

        user = get_user_model().objects.create(
            #create 하고 나면 생성된 user를 반환 하니까 user=로 정의 해줘야함
            email=email,
            username=username,
            password=data.get("password"),
            gender=data.get("gender"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            birthday=data.get("birthday"),
        )
        #오른쪽에 있는건 요청 받은 데이터(request.data)이고,
        #왼쪽에 있는건 해당 데이터를 가지고 생성된 사용자 객체(user)의 필드를 의미한다!

        return Response(
            {"id": user.id,  #"id"라고 하는것은 객체(user)의 id를 의미한다는 말!
             "email": user.email,  #"email"이라고 하는것은 객체(user)의 email을 의미한다는 말!
             "username": user.username,  #"username"이라고 하는것은 객체(user)의 username을 의미한다는 말!
             },
            status=201,  #요청받은 데이터를 성공적으로 처리해서 새로운 리소스를 생성한 상태를 나타냄!
        )


#    class LoginAPIView(APIView):
#        def get(self, request):
#            data = request.data
#''''' 이렇게 적어줘도 되지만, TokenObtainPairView.as.view()를 이용 하면 노필요!!


class UserDetailAPIView(APIView):
    def get(self, request, username):
        #if not get_user_model().objects.get(username=username).exists():
        #    return Response({"error": "username does not exists"}, status=400)
        #예외를 적용해야하는 상황이 생길때마다 if not..exists()를 이용해서 예외상황을 적용해줘도 되지만,
        #반복적으로 같은 코드가 사용되는건 좋지않기때문에 import get_object_or_404를 이용

        user = get_object_or_404(get_user_model(), username=username)
        #특정 객체를 가져올 때 사용 되는 형태!
        #username이 주어진 사용자를 가져오거나, 주어진 조건을 만족하지 않는 경우 404 Not Found 오류를 발생
        #조건(username)
        serializer = UserSerializer(user)
        return Response(
            #{    "id": user.id,
            #    "email": user.email,
            #    "username": user.username,
            #    "name": user.first_name + " " + user.last_name,
            #띄어쓰기를 하려면 ""를 활용 (큰따옴표 사이에 공백)하면 된다!
            #    "birthday": user.birthday,}
            #user.=> 아까 요청받았던 user에 정의 되어있는 value 값을 불러와!

            serializer.data
            #위에 정의해준 serializer의 데이터를 불러와줘!
            #(serilaizers.py에 정의해둔 UserSerializer의 fields(조건을 나타낼 때 사용)에서 요청하는 내용들
        )

# Create your views here.
# @api_view(["GET"])
# def json_profile(request): #아직도 함수 이름 짓기 어려워,,,OMG 사실 다어려움
#     accounts =User.objects.all()
#     serializer=UserSerializer(accounts,many=True)
#     return Response(serializer.data)
#    json_profile_list = []
#     for account in accounts:
#         json_profile_list.append({
#             "email":account.email,
#             "username":account.username,
#             "password":account.password,
#             "name":account.name,
#             "nickname":account.nickname,
#             "gender":account.gender,
#             "introduce":account.introduce,
#         })
#         return JsonResponse(json_profile_list,safe=False)

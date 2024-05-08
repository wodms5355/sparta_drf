from itertools import product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
#django global에 지정 되어있는 함수 Paginator!
from rest_framework.response import Response
from .serializers import CommentSerializer, ProductSerializer
from .models import Comment, Product
from rest_framework import status
from rest_framework.views import APIView


class ProductListAPIView(APIView):  # APIView가 갖고 있는 기능이 많다!
    #pagenaition을 사용하기 위해서는

    def get(self, request):
        #<상품목록조회>

        # self = 해당 메서드가 클래스의 인스턴스에 속하고 있다는 의미
        #request = 클라이언트로부터의 HTTP 요청을 처리하고 요청받은 데이터를 사용하기 위해
        # drf에서 crud 메소드 호출할때 self와 request는 기본값, 필요에 따라 pk도 +@로 작성
        products = Product.objects.all()  # Product models.py 안에 있는 모든것
        paginator = Paginator(products, 2)
        # paginator라는 변수를 지정
        #Paginator라는 함수를 import해줬음 근데 이건 global django에서(내장함수) 가져온거임!
        #Paginator이라는 class안에 들어있는 함수(매직메소드)/def __init__(self, object_list, per_page)=> 얘네는 필수!
        page = paginator.get_page(paginator)

        serializer = ProductSerializer(page, many=True)
        #serializer = ProductSerializer(products, many=True)
        # get은 목록을 읽는것이기 때문에 하나만 보여주는게 아니라서 many를 넣어줘야함
        return Response(serializer.data)
        # 바로 위에서 정의해놓은 serializer의 data값을 호출해

    def post(self, request):  #<상품생성>
        # self = 해당 메서드가 클래스의 인스턴스에 속하고 있다는 의미
        #request = 클라이언트로부터의 HTTP 요청을 처리하고 요청받은 데이터를 사용하기 위해
        username = request.data.get('username')  #이름
        title = request.data.get('title')  #제목
        content = request.data.get('content')  #내용
        image = request.data.get('image')  #이미지
        #요청받은 데이터에서 "name","title","context","image" 값을 가져와서 각각의 이름으로 다시 정의
        #왼쪽에 있는 "name","title","context","image"는 각각 클라이언트가 POST 요청을 보낼 때 사용한 데이터의 키 값
        #오른쪽에 있는 "name","title","context","image"는 각각 요청 받은 데이터

        if not (username and title and content and image):
            #=이중 하나라도 없다면
            return Response({"error": "Where are name,title,content,image?"}, status=400)
        #""의 내용을 보여주고, 400상태라는 걸 알려줘!

        porduct = Product.objects.create(
            #product=Product 클래스에서 생성한 name,title,content,image에 대한 값
            username=username,
            title=title,
            content=content,
            image=image,
        )
        serializer = ProductSerializer(product)  #product는 위에서 정의한 값
        #serializer이라고 정의된것은,
        # models.py에 정의된 product에 담긴 내용을 ProductSerializer에 맞는 조건에 대한 값
        return Response(serializer.data, status=201)
        #serializer를 통해 직렬화 한 데이터를 보여줘 그리고 성공적으로 생성 됐다는 상태를 보여줘

        #{
        #    'login_status': porduct.login_status,
        #    'name': porduct.name,
        #    'title': porduct.title,
        #    'context': porduct.context,
        #    'image': porduct.image.url,
        #    },
        #이렇게 각각 정의해줘도 되지만, serializers.py를 이용하면 코드를 간결하게 표현할 수 있다!

    def post(self, request):
        # 생성하는 매소드(=create)
        serializer = ProductSerializer(data=request.data)
        # 직렬화! Product class안에 있는 값들을 data로 불러와서 직렬화(요청 받은 데이터값을 데이터라고 하자!)
        if serializer.is_valid(raise_exception=True):  # 단, 모두 다 생성할 수는 없으니 조건이 붙음. 예외적용도 가능 (무슨 예외적용인지 한번더 질문하기)
            serializer.save()  # 모든것의 기본은 저-장!
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # post 메소드를 통해 잘 생성 됐으면 결과 도출! serializer의 데이터를 불러오고, 잘 생성된 결과 상태를 보여줘!


class ProductDetailAPIView(APIView):
    # pk가 작성됐다면 detail?!

    def get_object(self, pk):
        #self = 해당 메서드가 클래스 인스턴스에 속하고 있다는 것을 의미
        #pk = API에서 특정 객체를 식별하고 조회할 때 사용!
        #그래서 detailview는 특정 객체를 겨냥해서 보여주기 때문에 pk값이 필요함

        return get_object_or_404(Product, pk=pk)  # 요청값(pk)이(가) 없다면 404에러를 보여 주라는 건가....?
        # product class에서 가져온 기본키가 pk!
        # 똑같은 코드를 반복적으로 사용하지 않기위해 같은 내용은 함수로 묶어줬음!

    def get(self, request, pk):  # 메소드 호출할때 self와 request는 기본값, 필요에 따라 pk도 +@로 작성
        products = self.get_object(pk)  # poducts 안에 있는 pk값
        serializer = ProductSerializer(products, many=True)  # get은 목록을 읽는것이기 때문에 하나만 보여주는게 아니라서 many를 넣어줘야함
        #QuerySets(전달 받은 모델의 객체 목록)을 확인 해줘야 하기 때문에도 many=True을 써야함.
        return Response(serializer.data)  # 바로 위에서 정의해놓은 serializer의 Product class의 데이터를 직렬화해서 보여줘라!

    def put(self, request, pk):  # self,request는 기본값 pk는 필요에 따라?
        products = self.get_object(pk)  # pk는 기본키! #수정할 값을 pk로 정해주는 것!
        # 위의 get 메소드에서 정의한 accounts는 all()이라서 s를 붙여준거!
        serializer = ProductSerializer(products, data=request.data, partial=True)  # Product class의 유효성 검사
        # 24번 라인에 정의한 앱...?,요청 받아올 데이터,partial=True를 붙이게 될 경우, 변경 원하는 정보만 보내고 그 정보만 변경해서 저장 가능하다!)
        # 여기서 궁금증,,, partial=True가 patch메소드 비스무리한 역할을 해준다는건가?
        if not request.pk == products.pk:
            return Response({"error": "권한 없는 사용자 입니다! 계정을 확인해주세요"}, status=status.HTTP_400_BAD_REQUEST)
        #만약 요청받은 기본키와 위의 get_object로 받아온 pk의 값이 일치하지 않으면 에러메세지를 보여줘

        if serializer.is_valid(raise_exception=True):
            serializer.save()  # 얘도 저장 필수
            return Response(serializer.data, status=200)
            # 정상적으로 수정이 이루어 졌다면, 유효성 검사가 완료된 데이터를 불러와죠!
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # 그렇지 않다면, 에러메세지를 보여줘

    def delete(self, request, pk):
        products = self.get_object(pk)
        products.delete()  # 위에서 정의한 pk를 가진 데이터를 delete메소드를 이용해 삭제해줘!
        data = {"pk": f"{pk} is deleted."}
        # f태그를 달면 요청한 값을 불러올 수 있어서, pk값을 따로 지정하지 않아도 컴퓨터가 알아서 불러다줌

        if not request.pk == products.pk:
            return Response({"error": "권한 없는 사용자 입니다! 계정을 확인해주세요"}, status=status.HTTP_400_BAD_REQUEST)
        # 만약 요청받은 기본키와 위의 get_object로 받아온 pk의 값이 일치하지 않으면 에러메세지를 보여줘

        return Response(data, status=status.HTTP_200_OK)
        # 요청한 것들이 삭제되면,서버가 정상적으로 응답했다는걸 보여줘!


class CommentListAPIView(APIView):

    def get(self, request, pk):
        products = get_object(pk=pk)
        # 함수형으로 만든 get_object를 사용하기 위해서 self.(=지금 내가 작성하고 있는 함수가 포함된 class를 나타냄)을 사용
        comments = products.comments.all()
        serializer = CommentSerializer(comments, many=True)  # 위에 all()이 있기 때문에 many 작성
        return Response(serializer.data)  # 위에 불러온 serializer로 직렬화된 data를 불러옴

    def post(self, request, pk):  # create메소드
        products = get_object(pk=pk)
        serializer = CommentSerializer(data=request.data)  # serializers.py의 클래스 데려오기
        if serializer.is_valid(raise_exception=True):  # 예외 값도 ok
            serializer.save(products=products)
            # 저장필수 앞의 account는 , 뒤의 account는 59번째줄
            # 모델의 객체 정보가 필요 하기 때문에!
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # 직렬화된 데이터 값을 불러오고, 생성 상태를 성공으로 보여주기


def get_object(comment_pk):  # 새로 요청을 받는게 아니기 때문에 request가 없음
    return get_object_or_404(Comment, pk=comment_pk)  # class Comment의 기본키를 해당 함수의 기본키로 명명


class CommentDetailAPIView(APIView):  # detail

    # 흠 근데 그렇게되면, 위의 CommentListAPIView class의 pk이도 comment_pk로 정해줘야하지 않나,,,>?

    def put(self, request, comment_pk):  # 새로운 요청을 받아서 수정하는 거기 때문에 request필수
        comment = get_object(comment_pk)
        # 수정할게 어떤건지 지정해주는거---> comment_pk중에서 요청들어오는걸 수정한다는 말
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        # 직렬화를 하는건, CommentSerializer class에 있는 내용이랑, 요청받은 데이터!
        # partial=True라면, 변경 원하는 정보만 보내고 그 정보만 변경해서 저장 가능!!
        if serializer.is_valid(raise_exception=True):
            # 직렬화 한 값이 예외라고 하더라도 괜찮!
            serializer.save()  # 저장을 해야 직렬화한 데이터를 반환할 수 있다!
            return Response(serializer.data)  # 요청받은 데이터를 직렬화해서 보여줘!

    def delete(self, comment_pk):  # 새로 요청을 받는게 아니기 때문에 request가 없음
        comment = get_object(comment_pk)  # comment테이블의 기본키를 말하는거야!
        comment.delete()  # 방금 들어온 comment_pk에 해당하는 값들을 삭제해줘!
        data = {"pk": f"{comment_pk} is deleted."}
        # f태그를 달면 요청한 값을 불러올 수 있어서, pk값을 따로 지정하지 않아도 컴퓨터가 알아서 불러줌
        return Response(data, status=status.HTTP_200_OK)
    # 불러온 data의 값이 기본키와 같다면,삭제! 정상적인 삭제가 완료되면 실행완료 상태를 보여줌

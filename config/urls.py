"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api-auth/', include('rest_framework.urls')),
#    path('account/<str:username>/', include('accounts.urls')),
]

if settings.DEBUG:
    #settings.py에 DEBUG=True로 정의되어 있음
    #장고에서의 DEBUG모드는 개발모드를 의미
    #프로젝트가 DEBUG모드 일때만 실행되도록 해줘! = 만약 프로젝트가 DEBUG모드이면 실행 해줘!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #개발 시에만 MEDIA_URL에 대한 파일 서빙을 활성화하고, 배포 시에는 비활성화 해달라는 뜻
    #보안을 위해서도 있지만 조금 더 개발을 편하게 하게하기 위해서!



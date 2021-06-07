"""APIProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from api.views import article_details, article_list
# from api.views import ArticleList, ArticleDetails


from api.views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


from django.contrib import admin
from django.urls import path, include  # include is for viewset and routers

from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details), #for function based API view

    # path('articles/', ArticleList.as_view()),  # for class based API view
    # path('articles/<int:id>/', ArticleDetails.as_view())

    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),
]

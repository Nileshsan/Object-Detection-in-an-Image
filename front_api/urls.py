from django.urls import path, include
from rest_framework.routers import DefaultRouter
from front_api import views


router = DefaultRouter()
router.register('Hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')

urlpatterns = [
     path('hello-view/', views.HelloApiView.as_view()),
     path('', include(router.urls))
]

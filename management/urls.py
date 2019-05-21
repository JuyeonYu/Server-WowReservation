from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import UserInfoView
from . import views

router = routers.DefaultRouter()
router.register('userlist', UserInfoView)

urlpatterns = [
    path('', include(router.urls)),
    path('userlist/userid/<str:name>', views.detail)
]
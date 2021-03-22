from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from ModelApp.views import UserViewSet,ManageUserView,PersonViewSet

router = routers.DefaultRouter()
router.register('persons', PersonViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(),name='myself'),
    path('', include(router.urls)),
]



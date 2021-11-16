from django.urls import include, path
from rest_framework import routers
from apis import views


router = routers.DefaultRouter()
router.register(r'grdnrsmodel', views.GrdnrViewSet)

urlpatterns=[
    path("", include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework'))
]
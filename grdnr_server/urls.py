"""grdnr_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# from . import views
from grdnr_server.views import tasks, views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    # path('create_data/', views.HelloView.as_view(), name='create_data'),
    # path('apis/', include('apis.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token-verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('', views.display_data),
    path('dashboard', views.dashboard, name="dashboard"),
    path('grdnr_profile/<int:pk>/', views.grdnr_profile_data, name="profile_data"),
    path('display_data/<int:pk>/', views.display_data, name="display_data"),
    # path('example_view', views.example_view, name="example_view"),
    #path('all_grdnr_info_data/<int:no>/', views.sorting_grdnr_info_data, name='sorting_grdnr_info_data'),
    path('grdnr_data/<int:pk>/', views.get_grdnr_data, name='grdnr_data'),
    path('grdnr/', views.get_All_grdnr_data, name='grdnr'),
    path('create_data_new_grdnr/', views.create_grdnr_data, name='create_data'),
    path('update_grdnr_data/<int:pk>/', views.api_update_grdnr_data, name="update_grdnr_data"),
    path('filter_by_address/<str:address>/', views.filter_address, name="filter_address"),
    path('get_account_detail', views.get_account_detail, name='get_account_detail'),
    path('get_client_info', views.get_client_info, name='get_client_info'),
    
    #API url
    # path('create_task', tasks.create_task, name='create_task'),
    path('api_get_all_tasks', tasks.api_get_all_tasks, name='api_get_all_tasks'),
    path('get_all_tasks_view', tasks.get_all_tasks_view, name='get_all_tasks_view'),
    path('get_order_tasks', views.get_order_tasks, name="get_order_tasks"),
    # path('update_task/<int:pk>/', tasks.update_task, name='update_task'),

    # path('get_one_tasks/<int:pk>/', tasks.get_one_tasks, name='get_one_tasks'),

    #users
    path('users/', include('users.urls')),
]

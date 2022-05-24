"""synchron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from rest_framework import routers

from users import  views as user_view
from team.api import views as team_view
from standup_card import views as standup_card_view
from syncup_board import views as syncup_board_view

router = routers.DefaultRouter()
router.register(r'users',user_view.UserViewSet)
router.register(r'teams',team_view.TeamViewSet)
router.register(r'standup-cards',standup_card_view.StandupcardViewSet)
router.register(r'syncup-boards',syncup_board_view.SyncupboardViewSet,basename='syncup-board')


schema_view = get_schema_view(
   openapi.Info(
      title="Synchron API",
      default_version='v1',
      description="Rest endpoints for Synchron API",
      terms_of_service="terms",
      contact=openapi.Contact(email="email@email.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('dj/admin/', admin.site.urls),
    path('dj/',include('authen.urls')),
    path('dj/api/',include('frontend.urls')), # frontend routes
    path('dj/api/',include(router.urls)), #all routes registered in router will be added through this
    path('dj/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('syncup-board/',include('syncup_board.urls')),
    # path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('standup_card/',include('standup_card.urls')),
    # path('team/',include('team.api.urls')),
    # path('user/',include('user.urls')),
    # path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
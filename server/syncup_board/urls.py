from django.urls import path, include
# from .views import syncupboard_view
from rest_framework.routers import DefaultRouter
from .views import StandupCardList
# router = DefaultRouter()
# router.register('data', syncupboard_view)

# urlpatterns=[
#     path('',include(router.urls))
# ]

urlpatterns = [
    path('filter/',StandupCardList.as_view()),
]

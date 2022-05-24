from django.urls import path,include
# from standup_card.views import standup_card_view, standup_card_id, standup_card_create
from .views import standupcard_view
from rest_framework.routers import DefaultRouter

# router =DefaultRouter()
# router.register('data', standupcard_view)

# urlpatterns = [
#     path('',include(router.urls))
#     # path('view/',standup_card_view),
#     # path('view/<int:pk>/',standup_card_id),
#     # path('create/',standup_card_create)
# ]

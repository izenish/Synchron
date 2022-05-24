from django.urls import path

from . import views

urlpatterns=[
    path('standup-cards/',views.list_standupCards ,name='standup_cards' )
]
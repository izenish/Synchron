from rest_framework import serializers
from django.core import serializers as dj_serializer
from team.models import Team
from django.contrib.auth.models import User

from users.serializers import UserListSerializer


class UserRelatedField(serializers.RelatedField):

    '''
        Custom realtional field:
        Describes exactly how the output representation should be generated from the model instance.

        See also:
        _________
        https://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields
    '''
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        # print("ASASDASDASDADASD",value)
        return str(value)
        # return dj_serializer.serialize('json',value) 

    def to_internal_value(self, data):
        return User.objects.get(username=data)


class TeamSerializer(serializers.ModelSerializer):

    '''
        Serializer class for listing and editing team/s
    '''

    ''' If you want to display user id of particular team'''
    # users = serializers.PrimaryKeyRelatedField(many=True,queryset=User.objects.all())

    ''' If you want user name of particular team. Easier to read from swagger'''    
    users = UserRelatedField(many=True,queryset=User.objects.all())

    ''' All field of users are returned. Use this when developing frontend '''
    # users = UserListSerializer(many=True)
    class Meta:
        model=Team
        fields=['id','created_at','updated_at','teamName','users','is_active']   
        'or use fields="__all__"'

    





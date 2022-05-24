from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from synchron.permission import isScrumMaster
from standup_card.permissions import IsTeamMemberOrReadOnly

from standup_card.models import StandupCard,Update
from standup_card.serializers import StandupCardSerializer,UpdateSerializer

class StandupcardViewSet(ModelViewSet):
    serializer_class = StandupCardSerializer
    queryset = StandupCard.objects.all()
    authentication_classes = [SessionAuthentication]
    http_method_names =['get','post','patch','delete','head','options']
    
    
    def get_permissions(self):
        scrum_master_only_actions = ['create','partial_update','update','destroy','standup_updates','deactivate_update']
        if self.action in scrum_master_only_actions:
            permission_classes = [IsAuthenticated,isScrumMaster,IsTeamMemberOrReadOnly]
        else:
            permission_classes = [IsAuthenticated,]
        return [permission() for permission in permission_classes]

    def get_object_or_404(self, pk):
        try:
            return StandupCard.objects.get(pk=pk)
        except StandupCard.DoesNotExist:
            raise Http404


    def destroy(self,request,pk=None):
        '''
            Deactivate the standup card by primary key.

            _
        '''
        StandupCard = self.get_object()
        StandupCard.is_active = False
        StandupCard.save()
        data = StandupCardSerializer(StandupCard,context={'request': request}).data
        return Response(data)

    @action(detail=True,methods=['post'],serializer_class=UpdateSerializer)
    def standup_updates(self,request,pk=None):
        '''
            Add a new update to standup_card

            _
        '''
        standup_card = self.get_object()
        user = get_object_or_404(User,pk=request.data['user_id'])
        try:

            #check if user is in team,
            # print((standup_card.syncup_board_id.team_id.users.all()))
            if standup_card.syncup_board_id.team_id.__class__.objects.filter(users = user).exists():
                created_update =Update(user_id=user,comment=request.data['comment'],standup_id=standup_card)
                created_update.save()
                return Response(StandupCardSerializer(standup_card).data)
            else:
                return Response({'detail':f'User: {str(user)} doesnot belong to team: {str(standup_card.syncup_board_id.team_id)}'})
        except IntegrityError:
            return Response({'detail':f'Updates for user:{str(user)} already exists.'})

    @standup_updates.mapping.patch
    def deactivate_update(self,request,pk=None):
        '''
            Deactivate the particular update of standup_card given the id of user

            _
        '''
        standup_card = self.get_object()
        user_id = request.data['user_id']
        try:
            update =  standup_card.updates.filter(id=id)
            update.is_active = False
            update.save()
        except Exception as e:
            return Response({'detail':f'{e}'})

        return Response(StandupCardSerializer(self.get_object()).data)
    
    @action(detail=True,methods=['patch'],serializer_class=UpdateSerializer)
    def edit_standup_update(self,request,pk=None):
        standup_card = self.get_object()
        try:
            Update.objects.filter(id=request.data['id'],standup_id=standup_card).update(comment=request.data['comment'])
        except Exception as e:
            return Response({'detail':f'{e}'})
        return Response(StandupCardSerializer(self.get_object()).data)
        
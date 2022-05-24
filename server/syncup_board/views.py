# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from syncup_board.models import SyncupBoard
from syncup_board.serializers import SyncupBoardSerializer

from standup_card.models import StandupCard
from standup_card.serializers import StandupCardSerializer

from synchron.permission import isScrumMaster






class SyncupboardViewSet(ModelViewSet):
    serializer_class = SyncupBoardSerializer
    queryset = SyncupBoard.objects.all()
    #allowed methods
    http_method_names = ['get','post','delete','head','options']
    authentication_classes = [SessionAuthentication,]

    def get_permissions(self):
        """
            Checks permission based on current action,request and target
            Instantiates and returns the list of permissions that this view requires.

            returns
            _______
            permission_classes : list
        """
        if self.action == 'list' or self.action == 'change_role':
            permission_classes = [IsAuthenticated,isScrumMaster,]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    
    def destroy(self,request,pk=None):
        '''
            Changes the active status of Board

            Returns
            _______
            data : JSON
                - JSON object of modified user

            
        '''
        board = get_object_or_404(SyncupBoard,pk=pk)
        board.is_active = False
        board.save()
        data = SyncupBoardSerializer(board).data
        print(data)
        return Response(data)
    
    # def retrieve(self, request, pk=None):
    #     instance = self.get_object()
    #     # query = request.GET.get('query', None)  # read extra data
    #     return Response()



# class StandupCardList(ListAPIView):
#     permission_classes = [IsAuthenticated,isScrumMaster,]
#     serializer_class = SyncupBoardSerializer


#     queryset = SyncupBoard.objects.all()
#     serializer_class = SyncupBoardSerializer
#     # filter_backends=[SearchFilter]
#     filter_backends = [DjangoFilterBackend]
#     '<-Basic SearchFilter '
#     # search_fields=['team_id__users__username']  
#     'UsingDjangoFilterBackend'
#     filterset_fields =['team_id__users__username','created_at']   


    
    '''Note the dateTimeField takes  "2022-05-03T08:57:17.421390Z" 
    as input but while searching it wont work and has been an issue in DRF forever so in order to make the search work 
    remove the T and insert a space inbetween as  "2022-05-03 08:57:17.421390Z"'''


class StandupCardList(ListAPIView):
    permission_classes = [IsAuthenticated,isScrumMaster,]
    serializer_class = StandupCardSerializer


    queryset = StandupCard.objects.all()
    serializer_class = StandupCardSerializer
    # filter_backends=[SearchFilter]
    filter_backends = [DjangoFilterBackend]
    '<-Basic SearchFilter '
    # search_fields=['team_id__users__username']  
    'UsingDjangoFilterBackend'
    filterset_fields =['syncup_board_id__team_id__users__username','created_at']   



# test=SyncupBoard.objects.get(team_id=2)
# print(test.standup_card(extraNote))
    


    # def get_queryset(self):
    #     # user=self.request.user
    #     # return SyncupBoard.objects.filter(team_id__users=user)
    #     queryset = SyncupBoard.objects.all()

    #     'Take Username as input'
    #     user=self.request.query_params.get('user',None)
    #     'Convert the corresponding Username to its equivalent ID because Filter only takes int as input'
    #     username=User.objects.get(username=user).id

    #     date=self.request.query_params.get('date',None)
    #     print(date)


    #     if user is not None:
    #         queryset = queryset.filter(team_id__users=username)

    #     if date is not None:
    #         queryset=queryset.filter(created_at=date)

    #     return queryset
 

    

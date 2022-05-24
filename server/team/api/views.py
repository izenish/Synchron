# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import Http404


from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from team.api.permissions import IsTeamMemberOrReadOnly
'''isScrumMaster checks wether the logged in user is a SM or not'''
from synchron.permission import isScrumMaster

from team.api.serializers import TeamSerializer
from team.models import Team



'Using ModelViewSet'
class TeamViewSet(viewsets.ModelViewSet):
    serializer_class=TeamSerializer
    queryset = Team.objects.all()
    authentication_classes = [SessionAuthentication, ]
    http_method_names =['get','post','patch','delete','head','options']
    
    def get_queryset(self):
        
        '''
            filter through query params and returns a filtered queryset that is then 
            used for different actions
            
        '''
        queryset = Team.objects.all()
        is_active = self.request.query_params.get('is_active')
        team_name = self.request.query_params.get('teamName')

        if is_active is not None:
            queryset = queryset.filter(is_active= (is_active))
        if team_name is not None:
            queryset = queryset.filter(teamName= (team_name))

        if not queryset:
            raise Http404
            
            
        return queryset

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        scrum_master_only_actions = ['create','partial_update','destroy','users']
        if self.action in scrum_master_only_actions:
            permission_classes=[IsAuthenticated,isScrumMaster,IsTeamMemberOrReadOnly]
        else:
            permission_classes=[IsAuthenticated] 
        return [permission() for permission in permission_classes]   

    
    def create(self,request):
        """
        Create a new team , also can add team members while creating

        _
        """

        team = Team(teamName=request.data['teamName'])
        users = User.objects.filter(id__in=request.data['users'])
        team.save()
        team.users.add(*users)
        return Response(TeamSerializer(team,context={'request': request}).data)

    def destroy(self,request,pk=None):
        """
        Deactivate Teams

        _
        """

        team = self.get_object()
        team.is_active = False
        team.save()
        data = TeamSerializer(team,context={'request': request}).data
        return Response(data)


    @action(detail=True,methods=['post'],permission_classes=[])
    def users(self,request,pk=None):
        """
        Add team member to a team

        _
        """
        team = self.get_object()
        users = User.objects.filter(id__in=request.data['users'])
        team.users.add(*users)
        return Response(TeamSerializer(team,context={'request': request}).data)

    @users.mapping.patch
    def remove_users(self,request,pk=None):
        """
        Remove team member from a team

        _
        """
        team = self.get_object()
        user = User.objects.filter(id__in=request.data['users'])
        try:
            team.users.remove(*user)
        except User.DoesNotExist:
            raise Http404
        except Exception as e:
            return Response({'detail':f'{e}'})
        
        return Response(TeamSerializer(self.get_object()).data)
        
 


'''The same thing can be done with the below methods
however they include more LinesOfCodes but do have more flexibility'''


'Using Viewset'
# class TeamViewSet(viewsets.ViewSet):
#     def list(self,request):
#         team=Team.objects.all()
#         serializer=TeamSerializer(team,many=True)
#         return Response(serializer.data)
    
#     def retrive(self,request,pk=None):
#         id=pk
#         if id is not None:
#             team=Team.objects.get(id=id)
#             serializer=TeamSerializer(team)
#             return Response(serializer.data)


#     def create(self,request):
#         serializer=TeamSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def update(self,request,pk):
#         id=pk
#         team=TeamSerializer.objects.get(pk=id)
#         serializer=TeamSerializer(team,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def partial_update(self,request,pk):
#         id=pk
#         team=TeamSerializer.objects.get(pk=id)
#         serializer=TeamSerializer(team,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def destroy(self,request,pk):
#         id=pk
#         team=Team.objects.get(pk=id)
#         team.delete()
#         return Response({'msg':'Data Deleted'})



'Using Basic view'
# @api_view(['GET','POST'])
# def team_view(request):
#     if request.method=='GET':
#         team=Team.objects.all()
#         serializer=TeamSerializer(team,many=True)
#         return Response(serializer.data)

#     if request.method=="POST":
#         serializer=TeamSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET'])
# def team_detail(request,pk):
#     if request.method=='GET':
#         team=Team.objects.get(pk=pk)
#         serializer=TeamSerializer(team)
#         return Response(serializer.data)




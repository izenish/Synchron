
from django.contrib.auth.models import User
from django.http import Http404
from django.utils.decorators import method_decorator

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer

from drf_yasg.utils import swagger_auto_schema


from authen.models import roles
from .serializers import  UserListSerializer,UserPartialUpdateSerializer

from synchron.permission import isScrumMaster
from .permission import IsAuthorOrReadOnly

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="List all users. [SM]",
    operation_summary="List all users. [SM]",
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Get a user by id. [Author]",
    operation_summary="Get a user by id. [Author]",
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="Update a user by Id [Author]",
    operation_summary="Update a user by Id [Author]",
))
class UserViewSet(viewsets.ModelViewSet):
    '''
        A viewset to perform User CRUD operations

    '''
    http_method_names =['get','patch','delete','head','options']
    authentication_classes = [SessionAuthentication, ]
    queryset = User.objects.all().order_by('username')
    # renderer_classes = [TemplateHTMLRenderer,JSONRenderer]
    template_name = 'list_users.html'

    serializer_classes = {
        'partial_update': UserPartialUpdateSerializer
    }
    default_serializer_class = UserListSerializer

    def get_serializer_class(self):
        '''
            Returns the class that sould be used for the serializer
            
            Use if we want different serializer class for different action.

        '''
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        """
            Checks permission based on current action,request and target
            Instantiates and returns the list of permissions that this view requires.

            returns
            _______
            permission_classes : list
        """
        if self.action == 'list' or self.action == 'change_role' or self.action == 'me':
            permission_classes = [IsAuthenticated,isScrumMaster]
        else:
            permission_classes = [IsAuthenticated,IsAuthorOrReadOnly,]
        return [permission() for permission in permission_classes]

    def get_object_or_404(self, pk):
        '''
            Returns user object if found else returns not found error
        '''
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @action(detail=False,methods=['get'])
    def me(self,request,pk=None):
        logged_user = request.user

        # return Response({
        #     'serializer':UserListSerializer(logged_user),'user':logged_user
        # })
        return Response(UserListSerializer(logged_user,context={'request': request}).data)



    def destroy(self,request,pk=None):
        """
        Changes the active status of user.[SM]

        Change the active status of user
        """

        user = self.get_object()
        user.is_active = False
        user.save()
        data = UserListSerializer(user,context={'request': request}).data
        return Response(data)

    @action(detail=True,methods=['patch'],permission_classes=(isScrumMaster,IsAuthorOrReadOnly,))
    def change_role(self,request,pk=None):
        """
        Change user role. [SM]
        
        Permissions : SM, AUTH
        """

        change_role = request.data['roles']
        user = self.get_object_or_404(pk)
        if(str(user.roles) == change_role):
            return Response({'detail':f'Your role is already {change_role}'})
        roles.objects.filter(user=user.id).update(role=change_role)
        user = self.get_object_or_404(pk)
        return Response(UserListSerializer(user,context={'request': request}).data)


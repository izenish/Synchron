from rest_framework import permissions
# import django.contrib.auth.models import User

''' To understand Custom Permissions:
https://testdriven.io/blog/custom-permission-classes-drf/'''


'''Custom Permission so that only ScrumMasters can create teams and edit their teams
NOTE:the scrum master must be a member of that team so as to make changes to that team'''
class IsTeamMemberOrReadOnly(permissions.BasePermission):
    '''
        Custom permission to check if user belong to a team, else read-only access is given
    '''
    def has_permission(self,request,view):  
        return True

    #only runs for post,put not for get
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if(request.user in obj.users.all()):
            '''.all method to view all attributes'''
            return True
       
        return False


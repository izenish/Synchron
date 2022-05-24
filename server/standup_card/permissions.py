from rest_framework import permissions

class IsTeamMemberOrReadOnly(permissions.BasePermission):
    '''
        Custom permission to only allow selected roles of users to edit it.
    '''
    def has_permission(self,request,view):
        return True
    def has_object_permission(self,request,view,obj):
        '''
            Check if user is scrum master or developer.
            If user is scrum master then allow all actions.
            If user is developer then allow read only actions.
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        if(obj.syncup_board_id.team_id.__class__.objects.filter(users=request.user).exists()):
            print("hello")
            return True
        return False
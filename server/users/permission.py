from rest_framework import permissions
class IsAuthorOrReadOnly(permissions.BasePermission):

    '''
        permission to check if the logged in user is author or not
        
        CONSTs:
            SAFE_METHODS: GET, OPTIONS, HEAD
    '''
    def has_permission(self,request,view):  
        return True

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


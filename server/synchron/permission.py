from rest_framework import permissions
# has_permission is called on all HTTP requests whereas, has_object_permission is called from DRF's method def get_object(self). Hence, has_object_permission method is available for GET, PUT, DELETE, not for POST request.

class isScrumMaster(permissions.BasePermission):
    '''
        Custom permission to check if user is scrum master
        
        
        See also:
        _________
        To know the diff between has_permission and has_object_permission read this thread,
        - https://stackoverflow.com/questions/43064417/whats-the-differences-between-has-object-permission-and-has-permission#:~:text=Those%20two%20different%20methods%20are,method%20def%20get_object(self)%20.


        Notes: (See this to understand permission methods)
        ______
        - If you override get_object method, then you have to manually call self.check_object_permission(self.request,obj)
          to be able to execute has_object_permission
        - has_object_permission is checked against the spicific row in model
          where as has_permission is checked for entire list
        - In order for has_object_permission to be checked, has_permission must return True.
            If it return false, the request will be denied
        
    '''
    def has_permission(self,request,view):  
        '''
            Checks if authenticated user is scrum master
        '''
        if request.user.roles and str(request.user.roles) == 'sm':
            return True
        return False

    
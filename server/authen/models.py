from django.db import models
from django.contrib.auth.models import User

role_choices = (('dev','developer'), ('sm', 'scrum master'))
class roles(models.Model):
    '''
        Model for roles of users.
        Role will be either developer or scrum master.
        Scrum master will be able to create new team.
        Scrum master will be able to add new user to team.
        scrum master will be able to add new board to team.
        scrum master will be able to add new task to board.
        scrum master will be able to add new sprint to team.
        scrum master will be able to add new user to sprint.
    '''
    user = models.OneToOneField(User, related_name='roles', on_delete=models.CASCADE)
    role = models.CharField(max_length=5, choices=role_choices, default='dev')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.role)

# Create your models here.

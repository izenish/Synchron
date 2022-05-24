from curses.ascii import US
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    teamName=models.CharField(max_length=20)
    # sync_id=models.ForeignKey()
    # teamId=models.AutoField(primary_key=True)
    # userId=models.ForeignKey(User,on_delete=models.CASCADE)
    users=models.ManyToManyField(User,related_name='teams',blank=True,through='TeamMember')
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.teamName)


class TeamMember(models.Model):
    '''
        - This is an intermediate model.
        - By default, django creates an intermediate class for many to many relationship. This is the only 
        way database knows many to many relationship. Here we use TeamMember as intermediate class using 
        through = 'TeamMember'
        - So to create unique team members in a given team, we need this little 'hack' that enforces 
            unique_together attribute between user and team.

        # Read this article
        https://stackoverflow.com/questions/49810782/adding-unique-key-to-many-to-many-field-in-django

    '''
    team_id = models.ForeignKey(Team,null=True,on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.team_id} : {self.user_id}'
    class Meta:
        unique_together = ('team_id','user_id',)

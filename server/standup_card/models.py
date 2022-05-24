from django.db import models
from syncup_board.models import SyncupBoard
from django.contrib.auth.models import User


class StandupCard(models.Model):

    
    sprint_id=models.IntegerField()
    release_cycle=models.CharField(max_length=50)
    syncup_board_id = models.ForeignKey(SyncupBoard,related_name='standup_card',null=True, on_delete=models.CASCADE)
    extraNote=models.TextField(blank=True,default='')
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Board Id : {self.syncup_board_id} of {self.updated_at}'



class Update(models.Model):
    comment=models.TextField(blank=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    standup_id=models.ForeignKey(StandupCard, related_name='updates',on_delete=models.CASCADE)   
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'user : {self.user_id} in standup {self.standup_id}'


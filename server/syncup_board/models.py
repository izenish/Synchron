from django.db import models
from team.models import Team
# from standup_card.models import StandupCard
# Create your models here.
class SyncupBoard(models.Model):
    team_id=models.OneToOneField(Team, related_name='team', on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # syncup_cards = models.ForeignKey(StandupCard,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

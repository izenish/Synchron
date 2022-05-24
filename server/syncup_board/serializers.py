
from rest_framework import serializers
from standup_card.models import StandupCard
from standup_card.serializers import StandupCardSerializer
from team.api.serializers import TeamSerializer
from .models import SyncupBoard

class SyncupBoardSerializer(serializers.ModelSerializer):
    '''
        Serializer for SyncupBoard model.
    '''

    team = TeamSerializer(many=False,read_only=True,source='team_id')
    standup_card = StandupCardSerializer(many=True,read_only=True)

    class Meta:
        model = SyncupBoard
        fields = ['id','is_active','created_at','updated_at','team','team_id','standup_card']
        # 'standup_cards'

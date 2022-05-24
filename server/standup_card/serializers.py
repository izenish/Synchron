from rest_framework.serializers import ModelSerializer
from dataclasses import field
from .models import StandupCard,Update

class UpdateSerializer(ModelSerializer):
    class Meta:
        model= Update
        fields = '__all__'


class StandupCardSerializer(ModelSerializer):
    ''' 
        Serializer for StandupCard model.
    '''
    # syncup_board = SyncupBoardSerializer(many=False,read_only=True,source='syncup_board_id')
    updates = UpdateSerializer(many=True, read_only = False)
    class Meta:
        model = StandupCard
        fields = ['id','sprint_id','release_cycle','created_at','updated_at','syncup_board_id','extraNote','is_active','updates']

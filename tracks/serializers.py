from rest_framework import serializers
from .models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'title', 'bpm', 'mp3_price', 'price',
                  'wav_price', 'key', 'in_cart', 'track_status',
                  'selected_type', 'artwork', 'sample_audio',
                  'mp3', 'wav']
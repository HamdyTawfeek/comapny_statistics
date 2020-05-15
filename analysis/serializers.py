from rest_framework import serializers

from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = (
            'id', 'date', 'channel', 'country', 'os', 'impressions',
            'clicks', 'installs', 'spend', 'revenue',
        )
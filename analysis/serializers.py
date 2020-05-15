from rest_framework.serializers import (ModelSerializer, DateField, 
                                        CharField, IntegerField,
                                        DecimalField)

from .models import Performance

class PerformanceSerializer(ModelSerializer):
    """
    Performance Metrics Data Serializer
    """
    date = DateField(required=False, allow_null=False)
    channel = CharField(required=False, allow_null=False)
    country = CharField(required=False, allow_null=False)
    os = CharField(required=False, allow_null=False)
    impressions = IntegerField(required=False, allow_null=False)
    clicks = IntegerField(required=False, allow_null=False)
    installs = IntegerField(required=False, allow_null=False)
    spend = DecimalField(required=False, max_digits=30, decimal_places=2, allow_null=False)
    revenue = DecimalField(required=False, max_digits=30, decimal_places=2, allow_null=False)
    

    class Meta:
        model = Performance
        fields = (
            'id', 'date', 'channel', 'country', 'os', 'impressions',
            'clicks', 'installs', 'spend', 'revenue',
        )

from rest_framework.serializers import (ModelSerializer, DateField, 
                                        CharField, IntegerField,
                                        DecimalField)
from .models import Performance


class PerformanceSerializer(ModelSerializer):
    """
    Performance Metrics Data Serializer
    """
    def __init__(self, *args, **kwargs):
        super(PerformanceSerializer, self).__init__(*args, **kwargs)

        if 'context' in kwargs:
            if 'request' in kwargs['context']:
                fields = kwargs['context']['request'].query_params.getlist('field', [])
                excluded = kwargs['context']['request'].query_params.getlist('exclude', [])
                existing = set(self.fields.keys())

                if fields:
                    included = set(fields)
                    for other in existing - included:
                        self.fields.pop(other)
                
                if excluded:
                    for field in excluded:
                        self.fields.pop(field)


    date = DateField(required=False, allow_null=False)
    channel = CharField(required=False, allow_null=False)
    country = CharField(required=False, allow_null=False)
    os = CharField(required=False, allow_null=False)
    impressions = IntegerField(required=False, allow_null=False)
    clicks = IntegerField(required=False, allow_null=False)
    installs = IntegerField(required=False, allow_null=False)
    spend = DecimalField(required=False, max_digits=30, decimal_places=2, allow_null=False)
    revenue = DecimalField(required=False, max_digits=30, decimal_places=2, allow_null=False)
    cpi = DecimalField(required=False, max_digits=30, decimal_places=2, allow_null=False)
    

    class Meta:
        model = Performance
        fields = '__all__'

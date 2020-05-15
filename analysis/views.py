from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter as DjangoOrderingFilter

from django.db.models import Sum
from .serializers import PerformanceSerializer
from .models import Performance


class MetricList(ListAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = (DjangoFilterBackend, DjangoOrderingFilter,)
    filterset_fields = {
        'date': ['gte', 'lte', 'exact', 'gt', 'lt'],
        'channel': ['exact'],
        'country': ['exact'],
        'os': ['exact']
    }
    ordering_fields = '__all__'


    def get_queryset(self):
        group_by = self.request.query_params.get('group_by', None)
        if group_by is None:
            return super().get_queryset()
        
        group_by = map(str.strip, self.request.query_params['group_by'].split(','))
        queryset = Performance.objects.all()
        queryset =  (queryset.values(*group_by)
                            .annotate(
                            clicks = Sum('clicks'),
                            impressions = Sum('impressions'),
                            installs = Sum('installs'),
                            revenue = Sum('revenue'),
                            spend = Sum('spend'))
        )
        return queryset


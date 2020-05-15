from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter as DjangoOrderingFilter

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


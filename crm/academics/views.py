from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Direction, Faculty, Group
from .serializers import DirectionSerializer, FacultySerializer, GroupSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.select_related('faculty')
    serializer_class = DirectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['faculty']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.select_related('direction__faculty')
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['direction', 'is_active']

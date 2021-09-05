from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectModelSerializer, MeasurementModelSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # TODO: добавьте конфигурацию для объекта


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementModelSerializer

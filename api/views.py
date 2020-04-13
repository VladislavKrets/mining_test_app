from rest_framework import viewsets
from api import serializers
from api import models


class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ResourceModelSerializer
    queryset = models.ResourceModel.objects.all()

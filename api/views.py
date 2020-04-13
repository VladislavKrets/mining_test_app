from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework import views
from rest_framework.response import Response
from api import serializers
from api import models
from django.db.models import F, FloatField

#for all resoures endpoints
class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ResourceModelSerializer
    queryset = models.ResourceModel.objects.all()

#for total_cost endpoint
class TotalCostApiView(views.APIView):
    def get(self, request):
        total_cost = models.ResourceModel.objects.all().aggregate(
                total=Sum(F('price') * F('amount'), output_field=FloatField()))['total'] or 0
        return Response(data={'total_cost': total_cost},
                        status=status.HTTP_200_OK)


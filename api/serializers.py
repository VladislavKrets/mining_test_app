from rest_framework import serializers
from api import models


class ResourceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResourceModel
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['cost'] = float(data['price']) * int(data['amount'])
        return data

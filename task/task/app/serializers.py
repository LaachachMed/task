from rest_framework import serializers
from .models import task_data


# our model serializer
class task_serializers(serializers.ModelSerializer):
    class Meta:
        model = task_data
        fields = ['id', 'timestamp','temperature','duration']
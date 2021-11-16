from rest_framework import serializers
from grdnr_server.models import models

class SerializationClassGrdnr(serializers.ModelSerializer):
    class Meta:
        model=models.GrdnrModel
        fields = '__all__'


class SerializationClassTask(serializers.ModelSerializer):
    class Meta:
        model=models.TaskModel
        fields = '__all__'


class SerializationClassImg(serializers.ModelSerializer):
    class Meta:
        model=models.ImageModel
        fields = '__all__'
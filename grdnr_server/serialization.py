from rest_framework import serializers
from grdnr_server.models import models

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model=models.GrdnrsModel
        fields = '__all__'


class SerializationClassTask(serializers.ModelSerializer):
    class Meta:
        model=models.TaskModel
        fields = '__all__'


class SerializationClassAssignTasks(serializers.ModelSerializer):
    class Meta:
        model=models.AssigningJobsModel
        fields = '__all__'
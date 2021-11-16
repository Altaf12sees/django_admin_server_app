from grdnr_server.serialization import SerializationClassTask
from grdnr_server.models import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests


def get_all_tasks_view(request):
    get_task_api = requests.get('http://127.0.0.1:8000/api_get_all_tasks')
    results = get_task_api.json()
    return render(request, '../templates/tasks.html', {'data':results})


# __________ Tasks APIs __________
# Create tasks
@api_view(['POST'])
def create_task(request):
    serializer = SerializationClassTask(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# update task
@api_view(['POST'])
def update_task(request,pk):
    task_data = models.TaskModel.objects.get(task_id=pk)
    serializer = SerializationClassTask(instance=task_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# get tasks
@api_view(['GET'])
def get_one_tasks(request,pk):
    results = models.TaskModel.objects.get(task_id=pk)
    serializer = SerializationClassTask(results, many=False)
    return Response(serializer.data)


# view all tasks
@api_view(['GET'])
def api_get_all_tasks(request):
    results = models.TaskModel.objects.all()
    serialize = SerializationClassTask(results,  many=True)
    return Response(serialize.data)
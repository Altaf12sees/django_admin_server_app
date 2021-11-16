from django.shortcuts import render
from django.http import HttpResponse

from apis.models import GrdnrModel
from rest_framework import viewsets
from rest_framework import permissions
from apis.serialization import SerializationClassGrdnr


class GrdnrViewSet(viewsets.ModelViewSet):
    pass
    # qset = GrdnrModel.objects.all()
    # serializer_class = SerializationClassGrdnr
    # permissions_class = [permissions.IsAuthenticated]


def index(request):
    return render(request, "apis/index.html")
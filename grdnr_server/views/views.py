from grdnr_server.serialization import SerializationClass, SerializationClassTask, SerializationClassAssignTasks
from grdnr_server.models import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests
from .forms import *
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from django.db.models import Q

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models import Sum



# dashboard
def dashboard(request):
    count_grdnr = models.GrdnrsModel.objects.count()
    count_active_grdnr = models.GrdnrsModel.objects.filter(grdnr_account_status='Active').count()
    count_inactive_grdnr = models.GrdnrsModel.objects.filter(grdnr_account_status='Not Active').count()
    count_tasks = models.TaskModel.objects.count()
    job_done = models.TaskModel.objects.filter(task_status="Completed").count()
    zone_area_count = models.GrdnrsModel.objects.values('grdnr_address').annotate(count=Count('grdnr_address'))

    return render(request, '../templates/dashboard.html', {
        'total_grdnr':count_grdnr, 
        'active_grdnr':count_active_grdnr,
         'inactive_grdnr':count_inactive_grdnr,
         'total_tasks':count_tasks,
         'job_done':job_done,
         'count_area':zone_area_count})


# display all data
def display_data(request, pk):
    order_task = models.AssigningJobsModel.objects.filter(grdnr_name_id=pk).order_by('assign_task_date')
    # getapis = requests.get('http://127.0.0.1:8000/grdnr/')
    # results = getapis.json()
    results = models.GrdnrsModel.objects.all()
    results1 = models.GrdnrsModel.objects.filter(id=pk)
    count_tasks = models.AssigningJobsModel.objects.filter(grdnr_name_id=pk).count()
    count_active_tasks = models.AssigningJobsModel.objects.filter(Q(grdnr_name_id=pk) & Q(task_status='Active')).count()
    count_completed_tasks = models.AssigningJobsModel.objects.filter(Q(grdnr_name_id=pk) & Q(task_status='Done')).count()
    return render(request, '../templates/grdnrs.html', {'data':results,
    'order_task':order_task,
    'count_tasks':count_tasks,
    'count_completed_tasks':count_completed_tasks,
    'count_active_tasks':count_active_tasks,
    'key':pk, 'results1':results1})


# grdnr's info
# def sorting_grdnr_info_data(request,no):
#     if(no == 5):
#         sorted_by_add = models.GrdnrsModel.objects.order_by('grdnr_address')
#     if(no == 3):
#         sorted_by_name = models.GrdnrsModel.objects.order_by('grdnr_name')
#     if(no == 2):
#         results = models.GrdnrsModel.objects.order_by('grdnr_joining_date')
#     if(no == 21):
#         results = models.GrdnrsModel.objects.order_by('-grdnr_joining_date')
#     if(no == 1):
#         results = models.GrdnrsModel.objects.order_by('grdnr_account_status')
#     if(no == 0):
#         # getapis = requests.get('http://127.0.0.1:8000/grdnr/')
#         # results = getapis.json()
#         results = models.GrdnrsModel.objects.all()
#     return render(request, '../templates/grdnrs_list.html', {'data':results, 'no':no})


# get grdnr profile detail
def grdnr_profile_data(request, pk):
    get_api_data = requests.get('http://127.0.0.1:8000/grdnr_data'+ '/'+str(pk))
    results = get_api_data.json()
    return render(request, '../templates/grdnr_profile.html', {'data':results})


#get order tasks list
def get_order_tasks(request):
    get_order_tasks = models.AssigningJobsModel.objects.all()
    return render(request, '../templates/order_tasks.html', {'data':get_order_tasks})

#get account info
def get_account_detail(request):
    get_account_data = models.AccountsModel.objects.all()
    get_transaction_data = models.AccountTransactionHistoryModel.objects.all()
    return render(request, '../templates/accounts.html', {'data':get_account_data, 'data1':get_transaction_data})

#get client info
def get_client_info(request):
    get_client_data = models.ClientsModel.objects.all()
    return render(request, '../templates/clients.html', {'data': get_client_data})

#____________All APIs____________
# get single GRDNR data
@api_view(['GET'])
def get_grdnr_data(request,pk):
    if request.method == 'GET':
        # print(request.get_port()) for port no
        results = models.GrdnrsModel.objects.get(id=pk)
        serialize = SerializationClass(results,  many=False)
        return Response(serialize.data)


# get all GRDNR data
@api_view(['GET'])
def get_All_grdnr_data(request):
    if request.method == 'GET':
        results = models.GrdnrsModel.objects.all()
        serialize = SerializationClass(results,  many=True)
        return Response(serialize.data)


# post data
@api_view(['POST'])
def create_grdnr_data(request):
    serializer = SerializationClass(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# update data
@api_view(['POST'])
def api_update_grdnr_data(request,pk):
    grndr_data = models.GrdnrsModel.objects.get(id=pk)
    serializer = SerializationClass(instance=grndr_data, data=request.POST, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# filter for address
def filter_address(request, address):
    results = models.GrdnrsModel.objects.filter(grdnr_address__icontains=address)
    return render(request, '../templates/grdnr_profile.html', {'data':results})


# get order tasks
# def api_order_tasks(request):
#     results = models.TaskAssignModel.objects.all()
#     serialize = SerializationClassAssignTasks(results,  many=True)
#     return Response(serialize.data)


from django.contrib import admin
from grdnr_server.models import models


admin.site.site_header = "GRDNR Admin"
admin.site.site_title = "GRDNR Admin Portal"
admin.site.index_title = "Welcome to GRDNR Admin Portal"
admin.site.site_url = '/dashboard'

@admin.register(models.GrdnrsModel)
class GrdnrsAdmin(admin.ModelAdmin):
    list_display = ("grdnr_name","grdnr_phone","grdnr_account_status")

@admin.register(models.TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display=("task_title", "task_status", "task_created_date")
    # def show_average(self, obj):
    #     from grdnr_server.models import models
    #     result = models.TaskModel.objects.filter(task_value=obj).aggregate(models.TaskModel("task_value"))
    #     return result["task_value"]

admin.site.register(models.GrdnModel)
admin.site.register(models.ClientsModel)
admin.site.register(models.AssigningJobsModel)
admin.site.register(models.AccountsModel)
admin.site.register(models.AccountTransactionHistoryModel)
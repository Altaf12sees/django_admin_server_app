from django.db import models
import random
from django.utils.timezone import datetime


class GrdnrsModel(models.Model):
    grdnr_idno = models.CharField(max_length=255)
    grdnr_name = models.CharField(max_length=100)
    grdnr_password = models.CharField(max_length=50)
    grdnr_phone = models.CharField(max_length=50)
    grdnr_address = models.CharField(max_length=100, blank=True)
    grdnr_profile_photo = models.ImageField(upload_to='uploads/', blank=True)
    grdnr_pcr_report = models.ImageField(upload_to='uploads/', blank=True)
    grdnr_vaccination_id = models.CharField(max_length=50, blank=True)
    grdnr_vaccination_status = models.CharField(max_length=50, blank=True)
    grdnr_skills = models.CharField(max_length=100, blank=True)
    grdnr_profession = models.CharField(max_length=100, blank=True)
    grdnr_language = models.CharField(max_length=100, blank=True)
    grdnr_resignation_date = models.DateField(blank=True)
    grdnr_joining_date = models.DateField(blank=True)
    grdnr_emirates_id_front = models.ImageField(upload_to='uploads/', blank=True)
    grdnr_emirates_id_back = models.ImageField(upload_to='uploads/', blank=True)
    grdnr_visa_copy = models.ImageField(upload_to='uploads/', blank=True)
    grdnr_driving_licence_front = models.ImageField(upload_to='uploads/', blank=True)
    grdnr_driving_licence_back = models.ImageField(upload_to='uploads/', blank=True)
    grdnr_account_status = models.CharField(max_length=50)

    def __str__(self):
        return self.grdnr_name
    

class ClientsModel(models.Model):
    client_id = models.BigAutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=50)
    client_address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.client_name}"


class TaskModel(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    task_title = models.CharField(max_length=100)
    task_detail = models.CharField(max_length=500)
    task_value = models.CharField(max_length=50)
    task_status  = models.CharField(max_length=50, blank=True)
    task_created_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.task_title}"


class AssigningJobsModel(models.Model):
    assign_task_id = models.BigAutoField(primary_key=True)
    assign_task_date = models.DateField(default=datetime.now)
    grdnr_name = models.ForeignKey(GrdnrsModel, on_delete=models.CASCADE, null=True, blank=True)
    task_title = models.ForeignKey(TaskModel, on_delete=models.CASCADE, null=True, blank=True)
    task_values = models.CharField(max_length=10, blank=True)
    task_details = models.CharField(max_length=200, blank=True, null=True)
    task_status = models.CharField(max_length=100, blank=True)
    task_start_date = models.DateField(default=datetime.now, blank=True)
    task_end_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.grdnr_name} || {self.task_title}"


account_status = (
    ('Active','Active'),
    ('Not Active','Not Active'),
    ('Suspended','Suspended'),)

def rndfnc():
    rnd_id = random.randint(100000, 999999)
    return rnd_id

class AccountsModel(models.Model):
    account_id = models.CharField(max_length=100, default=rndfnc())
    grdnr_name = models.ForeignKey(GrdnrsModel, on_delete=models.CASCADE, null=True, blank=True)
    current_balance = models.CharField(max_length=10)
    credit_amount = models.CharField(max_length=10)
    debit_amount = models.CharField(max_length=10)
    agent_account_status = models.CharField(max_length=50, choices=account_status, default='Active')

    def __str__(self):
        return f"{self.account_id} || {self.grdnr_name}"


transaction_type_choices = (
    ('None', 'None'),
    ('Debit', 'Debit'),
    ('Credit', 'Credit')
)
transaction_mode = (
    ('Cash','Cash'),
    ('Online Transfer', 'Online Transfer'),
    ('Bank Transfer', 'Bank Transfer'),
    ('Other', 'Other')
)
class AccountTransactionHistoryModel(models.Model):
    transaction_type = models.CharField(max_length=100, choices=transaction_type_choices, default='None')
    transaction_amount = models.CharField(max_length=100, blank=True)
    account_id = models.ForeignKey(AccountsModel, on_delete=models.CASCADE, null=True, blank=True)
    grdnr_name = models.ForeignKey(GrdnrsModel, on_delete=models.CASCADE, null=True, blank=True)
    assign_task_id = models.ForeignKey(AssigningJobsModel, on_delete=models.CASCADE, null=True, blank=True)
    transaction_description = models.CharField(max_length=200)
    transaction_date = models.DateField(default=datetime.now, blank=True)
    transaction_mode = models.CharField(max_length=100, choices=transaction_mode, default='None')
    def __str__(self):
        return f"{self.grdnr_name} || {self.transaction_type} || {self.transaction_amount}"

class GrdnModel(models.Model):
    grdn_id = models.CharField(max_length = 100)
    grdn_name = models.CharField(max_length = 200)
    grdn_location = models.CharField(max_length = 500)
    grdn_type = models.CharField(max_length = 100)


# class CustomerSupportModel(models.Model):
#     ticket_id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     details = models.CharField(max_length=255)
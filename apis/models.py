# from django.db import models
# import random

# class GrdnrModel(models.Model):
#     grdnr_pk = models.BigAutoField(primary_key=True)
#     grdnr_id = models.CharField(max_length=255)
#     grdnr_name = models.CharField(max_length=100)
#     grdnr_password = models.CharField(max_length=50)
#     grdnr_phone = models.CharField(max_length=50)
#     grdnr_address = models.CharField(max_length=100, blank=True)
#     grdnr_profile_photo = models.ImageField(upload_to='uploads/', blank=True)
#     grdnr_pcr_report = models.ImageField(upload_to='uploads/', blank=True)
#     grdnr_vaccination_id = models.CharField(max_length=50, blank=True)
#     grdnr_vaccination_status = models.CharField(max_length=50, blank=True)
#     grdnr_skills = models.CharField(max_length=100, blank=True)
#     grdnr_profession = models.CharField(max_length=100, blank=True)
#     grdnr_language = models.CharField(max_length=100, blank=True)
#     grdnr_resignation_date = models.DateField(blank=True)
#     grdnr_joining_date = models.DateField(blank=True)
#     grdnr_emirates_id_front = models.ImageField(upload_to='uploads/', blank=True)
#     grdnr_emirates_id_back = models.ImageField(upload_to='uploads/', blank=True)
#     grdnr_visa_copy = models.ImageField(upload_to='uploads/', blank=True)
#     grdnr_driving_licence_front = models.ImageField(upload_to='uploads/', blank=True)
#     grdnr_driving_licence_back = models.ImageField(upload_to='uploads/', blank=True)
#     grdnr_account_status = models.CharField(max_length=50)

#     def __str__(self):
#         return self.grdnr_name


# class TaskModel(models.Model):
#     task_id = models.BigAutoField(primary_key=True)
#     task_title = models.CharField(max_length=100)
#     task_detail = models.CharField(max_length=500)
#     task_value = models.CharField(max_length=50)
#     task_status  = models.CharField(max_length=50, blank=True)
#     def __str__(self):
#         return self.task_title

    
# class GrdnModel(models.Model):
#     grdn_id = models.CharField(max_length = 100)
#     grdn_name = models.CharField(max_length = 200)
#     grdn_location = models.CharField(max_length = 500)
#     grdn_type = models.CharField(max_length = 100)


# def IdGenerating():
#     rnd_no = str(random.randint(10000, 99999))
#     return rnd_no


# class ImageModel(models.Model):
#     img_name = models.CharField(max_length=100)
#     img_file = models.ImageField(upload_to='uploads/', blank=True)

#     def __str__(self):
#         return self.img_name
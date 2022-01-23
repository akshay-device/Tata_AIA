from django.db import models


# Create your models here.

class tata_rec(models.Model):
    Ticket_ID = models.IntegerField(primary_key=True,auto_created=True)
    Date_of_Issue = models.DateField(null=True, blank=True , default=None)
    Time_of_Issue = models.TimeField(null=True, blank=True, default=None)
    Form = models.CharField(max_length=500, null=True, blank=True, default=None)
    Method = models.CharField(max_length=500, null=True, blank=True, default=None)
    Issue = models.CharField(max_length=500, null=True, blank=True, default=None)
    Caller_ID_Number = models.CharField(max_length=500, null=True, blank=True, default=None)
    Type_of_Call_or_Messge = models.CharField(max_length=500, null=True, blank=True, default=None)
    Advertiser_Business_Number = models.CharField(max_length=500, null=True, blank=True, default=None)
    City = models.CharField(max_length=500, null=True, blank=True, default=None)
    State = models.CharField(max_length=500, null=True, blank=True, default=None)
    Zip = models.IntegerField(default=None,null=True, blank=True)
    Location_Center_point_of_the_Zip_Code = models.CharField(max_length=500, null=True, blank=True, default=None)

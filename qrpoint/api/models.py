from django.db import models

# Create your models here.

class Employer(models.Model):
    employer_name   = models.CharField(max_length=25)
    employer_code   = models.CharField(max_length=25)
    member_count    = models.IntegerField()
    thumbnail       = models.CharField(max_length=200)
    register_date   = models.CharField(max_length=8)

class MemberData(models.Model):
    father  = models.CharField(max_length=25)
    mother  = models.CharField(max_length=25)
    hand    = models.BooleanField(default=False)

class Member(models.Model):
    member_name             = models.CharField(max_length=25)
    member_code             = models.IntegerField()
    member_personal_data    = models.ForeignKey(MemberData, on_delete=models.CASCADE)

class MedicalLicense(models.Model):
    initial_date    = models.CharField(max_length=8)
    final_date      = models.CharField(max_length=8)
    time            = models.IntegerField()
    member_code     = models.IntegerField() 
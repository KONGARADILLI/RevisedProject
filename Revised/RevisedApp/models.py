from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
	t=[('CSE','CSE'),('ECE','ECE'),('CIVIL','CIVIL'),('Mechanical','Mechanical'),('EEE','EEE'),('MBA','MBA')]
	y=[('III','III'),('IV','IV')]
	rollno=models.CharField(default='17AK1A000',max_length=10)
	dob=models.DateField(null=True)
	year=models.CharField(choices=y,max_length=5,null=True)
	dept=models.CharField(choices=t,max_length=12,null=True)
	phone_no=models.IntegerField(max_length=10,null=True)
	percentage=models.IntegerField(max_length=2,null=True)
	backlogs=models.IntegerField(max_length=2,null=True)
	pass_year=models.IntegerField(max_length=4,null=True)
	address=models.CharField(max_length=250,null=True)
	r=[(1,'student'),(2,'guest')]
	role=models.IntegerField(choices=r,default=2)

class Jobinfo(models.Model):
	title=models.CharField(max_length=25)
	location=models.CharField(max_length=20)
	salary=models.IntegerField(max_length=5,null=True)
	skills=models.CharField(max_length=30)
	job_role=models.CharField(max_length=30)
	eligible_percent=models.IntegerField(max_length=2,null=True)
	eligible_dept=models.CharField(max_length=30)
	year_of_pass=models.IntegerField(max_length=10,null=True)
	last_date=models.DateField(null=True)
	descrip=models.CharField(max_length=250)
	com_image=models.ImageField(upload_to='Jobs/',default='123.jpg')


# class ImProfile(models.Model):
# 	g=[('M','Male'),('F','Female')]
# 	age=models.IntegerField(default=21)
# 	impf=models.ImageField(upload_to='Profiles/',default="123.png")
# 	gender=models.CharField(max_length=10,choices=g)
# 	uid=models.OneToOneField(User,on_delete=models.CASCADE)

# @receiver(post_save,sender=User)
# def createpf(sender,instance,created,**kwargs):
# 	if created:
# 		ImProfile.objects.create(uid=instance)


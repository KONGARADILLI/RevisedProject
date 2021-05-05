from django import forms
from django.contrib.auth.forms import UserCreationForm
from RevisedApp.models import User,Jobinfo

class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=["username"]
		widgets={
		 "username":forms.TextInput(attrs={"class":"form-control","placeholder":"username"}),

		}

class Usperm(forms.ModelForm):
	class Meta:
		model = User
		fields=["username","role"]
		widgets={
		 "username":forms.TextInput(attrs={"class":"form-control","readOnly":True,}),
		 "role":forms.Select(attrs={"class":"form-control"}),
		}

class Jobform(forms.ModelForm):
	class Meta:
		model= Jobinfo
		fields = ["title","location","salary","job_role","skills"]
		widgets={
		"title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter company name"}),
		"location":forms.TextInput(attrs={"class":"form-control","placeholder":"Job Location"}),
		"salary":forms.NumberInput(attrs={"class":"form-control","placeholder":"Salary"}),
		"job_role":forms.TextInput(attrs={"class":"form-control","placeholder":"Job Role"}),
		"skills":forms.TextInput(attrs={"class":"form-control","placeholder":"Skills requried"}),
		}
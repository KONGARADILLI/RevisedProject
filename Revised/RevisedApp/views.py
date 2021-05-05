from django.shortcuts import render,redirect
from RevisedApp.forms import UsForm,Usperm,Jobform
from django.core.mail import EmailMessage
from Revised import settings
from RevisedApp.models import User

# Create your views here.

def homepage(request):
	return render(request,'html/home.html')

def register(request):
	if request.method=="POST":
		t=UsForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/lg')
	y=UsForm()
	return render(request,'html/register.html',{'t':y})

def role(request):
	return render(request,'html/mp.html')

def requestform(request):
	if request.method == "POST":
		u=request.POST.get('username')
		r=request.POST.get('rollno')
		d=request.POST.get('dept')
		e=request.POST.get('email')
		at=request.FILES['fe']
		y="Regarding approve request of "+u
		# t= mail_admins("Usesr Role",y)
		t=EmailMessage("Usesr approval",y,settings.EMAIL_HOST_USER,[settings.ADMINS[0][1],e])
		t.content_subtype= 'html'
		t.attach(at.name,at.read(),at.content_type)
		t.send()
		if t == 1:
			return redirect('/req')
	return render(request,'html/request.html')

def permissions(request):
	ty=User.objects.all()
	return render(request,'html/permissions.html',{'q':ty})

def gvper(request,k):
	r=User.objects.get(id=k)
	if request.method == "POST":
		k=Usperm(request.POST,instance=r)
		if k.is_valid():
			k.save()
			return redirect('/per')
	k2= Usperm(instance=r)
	return render(request,'html/gvp.html',{'y':k2})

def dashboard(request):
	return render(request,'html/dashboard.html')

def jobposts(request):
	t=Jobform()
	return render(request,'html/jobs.html',{'y':t})
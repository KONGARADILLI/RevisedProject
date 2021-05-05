from django.urls import path
from RevisedApp import views
from django.contrib.auth import views as ad  

urlpatterns=[

path('',views.homepage,name='home'),
path('lg/',ad.LoginView.as_view(template_name="html/login.html"),name='log'),
path('lgout/',ad.LogoutView.as_view(template_name="html/logout.html"),name='logo'),
path('reg/',views.register,name='reges'),
path('rol/',views.role,name='main'),
path('req/',views.requestform,name='request'),
path('per/',views.permissions,name='perm'),
path('eper/<int:k>',views.gvper,name='gp'),
path('das/',views.dashboard,name='dash'),
path('jobs/',views.jobposts,name='job'),
]
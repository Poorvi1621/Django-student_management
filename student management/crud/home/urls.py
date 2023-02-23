
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path("",views.index),
    path('ulogin/',views.ulogin),
    path('uregs/',views.uregs),
    path('signup/',views.signup),
    path('welcome/',views.welcome),
    path('courses/', views.courses, name='courses'),
    path('addcourses/', views.addcourses, name='addcourses'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('viewstudents/',views.viewstudents),
    path('delete/',views.delete),
    path('update_view/<int:uid>',views.update_view),
    path('update_course/',views.update_course),
    path('profile/',views.profile)
    path('addteacher/',views.addteacher)
]

from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'gym'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('register/', views.register, name='register'),
    url(r'^About/$', views.About, name='About'),
    path('contact/', views.contact, name='contact'),
    url ( r'^calendar/$' , views.CalendarView.as_view ( ) , name='calendar' ) ,
    url ( r'^event/new/$' , views.event_new , name='event_new' ) ,
    url ( r'^event/edit/(?P<event_id>\d+)/$' , views.event_edit , name='event_edit' ) ,
    path ( r'^event/<int:pk>/delete/' , views.event_delete , name='event_delete' ) ,
    url ( r'^customercalendar/$' , views.CalendarCustomerView.as_view ( ) , name='customercalendar' ) ,
    path('CustomerViewActivities', views.CustomerViewActivities, name='CustomerViewActivities'),
    path('admin/users_list', views.users_list, name='users_list'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<username>/delete/', views.user_delete, name='user_delete'),
    path('user/create/', views.user_new, name='user_new'),
    url(r'^reports_list/$', views.reports_list, name='reports_list'),
    path('user_summary_pdf', views.user_summary_pdf, name='user_summary_pdf'),
    path('activities_summary_pdf', views.activities_summary_pdf, name='activities_summary_pdf'),
    path('equipment_list', views.equipment_list, name='equipment_list'),
    path('equipment/<int:pk>/edit/', views.equipment_edit, name='equipment_edit'),
    path('equipment/<int:pk>/delete/', views.equipment_delete, name='equipment_delete'),
    path('equipment/create/', views.equipment_new, name='equipment_new'),
    path('CustomerViewEquipments', views.CustomerViewEquipments, name='CustomerViewEquipments'),
    path('equipment_summary_pdf', views.equipment_summary_pdf, name='equipment_summary_pdf'),


    ]

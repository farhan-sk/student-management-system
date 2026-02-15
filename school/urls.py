from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index, name="index"),
   path('dashboard/', views.dashboard, name='dashboard'), 
   path('notification/mark-as-read/', views.mark_notification_as_read, name='mark_notification_as_read' ),
   path('notification/clear-all', views.clear_all_notification, name= "clear_all_notifications"),
   path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
   path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
   path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
   path('ai-chat/', views.ai_assistant, name='ai_chat'),
   path('ai-chat-page/', views.ai_chat_page, name='ai_chat_page'),

]

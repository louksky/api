from django.urls import path
from . import views

urlpatterns = [
	path('', views.api_views, name="Asaf api-views"),
	path('msg-write/',views.msg_write,name='msg-write'),
	path('msg-list',views.msg_List,name='msg-list'),
	path('un-msg-list',views.msgunread_List,name='un-msg-list'),
	path('msg-read/<str:pk>/',views.msg_read,name='msg-read'),
	path('msg-delete/<str:pk>/', views.msg_delete, name="msg-delete"),
]

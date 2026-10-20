from django.urls import path
from . import views

urlpatterns = [
	path('', views.show_list, name='show_list'),
	path('add/', views.add_show, name="add_show"),
	path('delete/<int:show_id>/', views.delete_show, name='delete_show'),
]


from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.add_show, name="add_show")
]


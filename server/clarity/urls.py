from django.urls import path
from . import views
	
urlpatterns = [
	path("index.html", views.index, name="index"),
	path("find_company.html", views.findcompany, name="find_company"),
	path("request_company.html", views.requestcompany, name="request_company")
]
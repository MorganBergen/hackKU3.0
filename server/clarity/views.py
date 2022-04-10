from pickletools import read_uint1
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "pages/index.html")

def findcompany(request):
	return render(request, "pages/find_company.html")

def requestcompany(request):
	return render(request, "pages/request_company.html")

'''

from django.conf import settings
from django.conf.urls.static import static



/pages/index.html
/pages/find_company.html
/pages/request_company.html
/pages/company_report.html
'''
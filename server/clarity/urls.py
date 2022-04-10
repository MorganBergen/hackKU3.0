from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
	
urlpatterns = [
	path("index.html", views.index, name="index"),
	path("find_company.html", views.findcompany, name="find_company"),
	path("request_company.html", views.requestcompany, name="request_company")
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROO)



'''
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
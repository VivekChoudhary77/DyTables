"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('createTable', views.createTable),
    path('myTable', views.myTables),
    path('getTable', views.getTable),
    path('addData', views.addData),
    path('deleteRow', views.deleteRow),
    path('updateRow', views.updateRow),
    path('filterData', views.filterData),
    path('auditHistory', views.auditHistory),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),

]
handler404 = views.handler404
handler500 = views.handler500

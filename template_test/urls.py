"""template_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from one import views as app1_views
from two import views as app2_views
from three import views as app3_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1_views.index_redirect),
    path('one/', app1_views.index, name="app1_index"),
    path('two/', app2_views.index, name="app2_index"),
    path('three/', app3_views.index, name="app3_index"),
]

"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include


urlpatterns = [
    path('', include('travel_app.urls')),
    path('admin/', admin.site.urls),
    path('gastro/', include('travel_app.urls')),
    path('activelist/', include('travel_app.urls')),
    path('about-us/', include('travel_app.urls')),
    path('transport/', include('travel_app.urls')),
    path('important/', include('travel_app.urls')),
    path('gori-i-poseleniya/', include('travel_app.urls')),
    path('kanyon/', include('travel_app.urls')),
    path('don/', include('travel_app.urls')),
    path('don1/', include('travel_app.urls')),
    path('kvadro3/', include('travel_app.urls'))

]


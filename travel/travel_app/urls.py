from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('activelist/', views.activepage),
    path('about-us/', views.about_us),
    path('transport/', views.transport),
    path('important/', views.important),
    path('gori-i-poseleniya/', views.goriIPoseleniya),
    path('kanyon/', views.kanyon),
    path('don/', views.don),
    path('don1/', views.don1),
    path('kvadro3/', views.kvadro3)

    # path('gastro', Gastro.as_view(), name='gastro'),
    # path('ethno', Ethno.as_view(), name='ethno'),
    # path('active', Active.as_view(), name='active'),
    # path('recreation', Recreation.as_view(), name='recreation')

]

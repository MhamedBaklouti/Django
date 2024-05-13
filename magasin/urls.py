from django.urls import path   #,include
# from django.conf.urls import url

from . import views

urlpatterns = [	
    path('', views.register,name='register'),
    path('add/', views.vitrine,name='vitrine'),
    path('update/', views.modifier,name='update'),
    path('register/',views.register, name = 'register'),

]

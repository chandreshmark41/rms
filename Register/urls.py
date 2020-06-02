from django.urls import path
from . import views
urlpatterns= [

    path('StudentRegister/', views.StudentRegister, name='StudentRegister'),
    path('AdminRegister/', views.AdminRegister, name='AdminRegister'),

]
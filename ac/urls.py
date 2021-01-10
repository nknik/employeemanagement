from django.urls import path
from . import views
from .views import viewmodel
from .views import editmodel,deletemodel

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('addemp', views.addemp, name='addemp'),
    path('viewmodel', views.viewmodel, name='viewmodel'),
    path('<id>/viewmodel',viewmodel),
    path('<id>/editmodel',editmodel),
    path('<id>/deletemodel',deletemodel),
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
]

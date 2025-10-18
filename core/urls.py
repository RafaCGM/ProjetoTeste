from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
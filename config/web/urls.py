from django.urls import path
from .views import *


urlpatterns = [
    path('search/', search_products, name='searched'),
    path('', products, name='all'),

]

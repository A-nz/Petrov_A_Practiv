from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('add_results/', AddRecord.as_view(), name='add_results')
]
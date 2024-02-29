from django.contrib import admin
from django.urls import path
from .views import CifApplication

urlpatterns = [
    path('cif/createCif', CifApplication.as_view(), name="createCifProfile"),
    path('cif/getCifDetails', CifApplication.as_view(), name='getCifDetails')
]
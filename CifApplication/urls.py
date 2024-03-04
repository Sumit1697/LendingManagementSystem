from django.urls import path
from .views import CifApplication

urlpatterns = [
    path('createCif', CifApplication.as_view(), name="createCifProfile"),
    path('getCifDetails', CifApplication.as_view(), name='getCifDetails')
]
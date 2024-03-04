from django.urls import path, include
from .views import AccountOnborading


urlpatterns = [
    path('account', AccountOnborading.as_view(), name="createAccount")
]
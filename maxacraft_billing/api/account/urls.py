from django.urls import path

from .views.get_account import GetAccountController

urlpatterns = [
    path('get', GetAccountController.as_view()),
]
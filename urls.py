from django.urls import path
from .views import landing_view
from.views import main_view

urlpatterns = [
    path('',landing_view,name='main')
]

from django.urls import path
from . import views



urlpatterns = [

    path('', views.multistepform, name='home'),
    path('results/', views.results, name="results")

]
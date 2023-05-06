from django.urls import path
from . import views



urlpatterns = [

    path('', views.SellerWizard.as_view(), name='home'),
    path('results/', views.results, name="results")

]
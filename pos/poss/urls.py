from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.dashbord, name='dashbord'),
    path('invoicing', views.invoicing, name='invoicing'),
    path('add_product', views.add_product, name='add_product'),
    path('inventory', views.inventory, name='inventory'),
]
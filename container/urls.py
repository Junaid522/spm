from django.urls import path
from container import views

urlpatterns = [
    path('container_details/',views.ContainerDetails.as_view(),name='container_details'),
    path('warehouse_details/',views.WarehouseDetails.as_view(),name='warehouse_details'),
    path('bilties/',views.Bilties.as_view(),name='bilties'),
]
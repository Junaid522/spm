from django.urls import path
from home import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('about_us/',views.AboutUs.as_view(),name='about_us'),
    path('contact_us/',views.ContactUs.as_view(),name='contact_us'),
]
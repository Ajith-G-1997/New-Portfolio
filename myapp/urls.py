from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.AboutPage,name='about'),
    path('resume/',views.Resume,name='resume'),
    path('services/',views.Services,name='services'),
    path('portfolio/',views.Portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
]

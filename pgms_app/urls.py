from django.urls import path
from django.urls import path
from pgms_app.views import *
from django.urls import path, re_path
from .views import index, profile, contact, register, register_now, confirm_now, reset_payment

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    re_path(r'^register_now/(?P<pk>\d+)$', register_now, name='register_now'),
    re_path(r'^confirm_now/(?P<pk>\d+)$', confirm_now, name='confirm_now'),
    path('reset_payment/', reset_payment, name='reset_payment'),
]


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apply/', views.apply, name='apply'),
    path('member-entry/', views.memberentry, name='memberEntry'),
    path('thank-you/', views.thankyou, name='thankyou'),
    # path('/signup', views.signUp, name='signUp'),
]

from django.urls import path
from .import views

urlpatterns = [
    path('',views.landing_page,name='landing_page'),
    path('signup_view/',views.signup_view,name='signup_view'),
    path('signin_view/',views.signin_view,name='signin_view'),

]
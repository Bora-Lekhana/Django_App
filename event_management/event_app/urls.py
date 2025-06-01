
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('register/success',views.register_success,name="register_success"),
    path('login/',views.login,name='login'),
    path('logout/', views.logout_view, name='logout'),
]

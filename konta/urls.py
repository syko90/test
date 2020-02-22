from django.urls import path
from . import views

app_name ='konta'

urlpatterns = [
    path('rejestracja/', views.rejestracja_widok, name='rejestracja'),
    path('logowanie/', views.login_view, name= 'login'),
    path('wylogowanie/', views.logout_view, name='logout')
    
]
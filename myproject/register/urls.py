from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.register_view, name='page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
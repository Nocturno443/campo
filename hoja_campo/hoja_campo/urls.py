from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"), 
    path('home_in/', views.home_in, name='home_in'),  
    path('profile_list/', views.profile_list, name='profile_list'),  
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_meep/<int:pk>', views.edit_meep, name='edit_meep'),
    path('search/', views.search, name='search'),
    path('listados/', views.listados, name="listados"),
]

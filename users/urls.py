"""Users URL Configuration"""

from django.urls import path
from users import views



urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/<str:username>/follow', views.follow, name='follow')
    

]


   
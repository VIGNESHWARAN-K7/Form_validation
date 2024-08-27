# accounts/urls.py
# from django.urls import path
from django.contrib.auth.views import LogoutView
# from . import views

# urlpatterns = [
#     path('', views.register, name='register'),
#     path("profile/",views.profile,name='profile'),
#     path("login/",views.login_page,name='login'),
#     path("logout/",views.logout_page,name='logout'),

# ]
# # accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]


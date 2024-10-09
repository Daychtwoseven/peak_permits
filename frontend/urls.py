from django.contrib.auth import views as auth_views
from django.urls import path
from . views import *


urlpatterns = [
    path('', index_page, name='frontend-index-page'),
    path('dashboard/', dashboard_page, name='frontend-dashboard-page'),
    path('request/', request_page, name='frontend-request-page'),
    path('login/', login_page, name='frontend-login-page'),
    path('logout/', auth_views.LogoutView.as_view(), name='frontend-logout-page'),
]

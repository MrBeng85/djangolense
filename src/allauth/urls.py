from django.urls import path
from .views import signup, login_view, logout_view

urlpatterns = [
    path('signup/', signup, name='account_signup'),
    path('login/', login_view, name='account_login'),
    path('logout/', logout_view, name='account_logout')
]
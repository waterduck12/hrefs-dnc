from django.urls import path, include
from .views import *
import accounts.views

app_name = 'accounts'

urlpatterns = [
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    # path('home/', accounts.views.home, sname='home'),
]
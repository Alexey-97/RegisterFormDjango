from django.urls import path
from .views import *

urlpatterns = [
    path('', registration, name='sign_up'),
    path('sign_in/', LoginUser.as_view(), name='sign_in'),
    path('home/', home, name='page_home'),
    

]

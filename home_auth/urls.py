from django.urls import path

from home_auth.views import signup_view, login_view, forgot_password_view, reset_password_view, logout_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('reset-password/<str:token>/', reset_password_view, name='reset_password'),
    path('logout/', logout_view, name='logout'),

]

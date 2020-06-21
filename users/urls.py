from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path
from .views import LoginView, LogoutView, ProfileView, PasswordChangeView, PasswordChangeDoneView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('register/', RegisterView.as_view(), name='register'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

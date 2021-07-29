from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('password/reset', views.PasswordResetView.as_view(), name="password_reset"),
    path('password/reset/email_sent', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password/reset/complete', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

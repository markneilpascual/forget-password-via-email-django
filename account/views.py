
from django.contrib.auth import views
from .forms import PasswordResetConfirmForm, PasswordResetForm


class LoginView(views.LoginView):
    template_name = 'account/auth/login.html'

class PasswordResetView(views.PasswordResetView):
    template_name = 'account/auth/password_reset.html'
    form_class = PasswordResetForm
    email_template_name = 'account/auth/includes/password_reset_email.html'
    subject_template_name = 'account/auth/includes/password_reset_subject.txt'

class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'account/auth/password_reset_confirm.html'
    form_class = PasswordResetConfirmForm


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'account/auth/password_reset_done.html'


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'account/auth/password_reset_complete.html'

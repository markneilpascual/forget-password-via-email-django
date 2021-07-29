# forget-password-via-email-django
# django-forget-password-via-email forget password via email authentication   ###### Install requirements  ``` pip install -r requirements.txt ```  ###### Migrate models ``` python manage.py makemigrations python manage.py migrate ``` ###### Set up email settings in settings.py  ```python EMAIL_HOST = '&lt;Email host>' EMAIL_USE_TLS = True EMAIL_PORT = &lt;Email server port> EMAIL_HOST_USER = '&lt;Your email server user>' EMAIL_HOST_PASSWORD = '&lt;Your email server password>'  ```  Setup `DEFAULT_FROM_EMAIL` for the email address of the email sender who will send the email. ```python DEFAULT_FROM_EMAIL  = '&lt;Email address of the sender>' ```  Alternatively, include `from_email` property in  `PasswordResetView` in views.py ```python class PasswordResetView(views.PasswordResetView) ... from_email = '&lt;Email address of the sender>' ```  ###### Changing email content  Changing email subject `account/templates/account/auth/includes/password_reset_subject.txt`  Changing email content `account/templates/account/auth/includes/password_reset_email.html`
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .forms import LoginForm
from .views import RegisterView

app_name = "app_users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(redirect_authenticated_user=True, template_name='app_users/login.html',
                                     authentication_form=LoginForm), name="login"),
    path("logout/", LogoutView.as_view(template_name='app_users/logout.html'), name='logout')
]

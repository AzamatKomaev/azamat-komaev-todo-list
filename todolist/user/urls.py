from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .services import anonymous_required
from . import views


urlpatterns = (
    path('registration', anonymous_required(views.RegistrationView.as_view()), name='user.registration'),
    path('login', anonymous_required(views.CustomLoginView.as_view()), name='user.login'),
    path('logout', login_required(LogoutView.as_view()), {'next_page': 'user.registration'}, name='user.logout'),
)

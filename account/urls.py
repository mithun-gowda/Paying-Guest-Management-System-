from django.urls import path, re_path
from account.views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup1'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login1'),
    path('logout/', auth_views.LogoutView.as_view(next_page='pgms1:index'), name='logout1'),
]
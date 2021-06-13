from re import template
from django.conf.urls import url
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^login_page/$', views.login_page, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),
  
	#Urls para o reset password
	url(r'password_reset/$',auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"),name='password_reset'),
    url(r'password_reset/done/$',auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"),name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html"),name='password_reset_confirm'),
    url(r'reset/done/',auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/reset_done.html"),name='password_reset_complete')

]

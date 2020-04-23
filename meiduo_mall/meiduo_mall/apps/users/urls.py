from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register/$',views.RegisterView.as_view()),
    url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,28})/count/$',views.UsernameCountView.as_view()),
    url(r'^mobiles/(?P<mobile>1[3456789]\d{9})/count/$',views.MobileCountView.as_view()),
    url('^login/$', views.LoginView.as_view()),
    url('^logout/$',views.LogoutView.as_view()),
    url('^info/$', views.UserCenterInfoView.as_view()),
    url('^emails/$', views.EmailView.as_view()),
    url('^emails/verification/$', views.EmailActiveView.as_view()),
    url('^addresses/$', views.AddressView.as_view()),
]
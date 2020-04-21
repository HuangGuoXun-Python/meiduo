from django.conf.urls import url

from . import views
import uuid

urlpatterns = [

    url('^image_codes/(?P<uuid>[\w-]+)/$', views.ImageCodeView1.as_view()),
]
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.custom, name='custom'),
    url(r'^suggetion/$', views.suggetion, name='custom')
];

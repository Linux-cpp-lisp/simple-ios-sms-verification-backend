from django.conf.urls import patterns, url

from verifier import views

urlpatterns = patterns('',
    url(r'^send-code/$', views.send_code, name='send_code'),
    url(r'^check-code/$', views.check_code, name="check_code")
) 

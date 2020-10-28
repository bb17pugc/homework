from django.conf.urls import include, url

from myapp.views import index

urlpatterns = [
    url('index', index, name='index')
    ]
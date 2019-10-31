from django.conf.urls import url
from .views import *
app_name = 'exam'
urlpatterns = [
    url(r'^start/$', calculator, name='calculator'),
]
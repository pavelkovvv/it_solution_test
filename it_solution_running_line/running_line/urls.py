from django.urls import path

from . import views

app_name = 'running_line'

urlpatterns = [
    path('', views.index, name='index_page'),
]
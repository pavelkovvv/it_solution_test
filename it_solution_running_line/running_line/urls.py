from django.urls import path

from . import views

app_name = 'running_line'

urlpatterns = [
    path('', views.index, name='index_page'),
    path('download/', views.download_video, name='download_video'),
    path('stats/', views.stats, name='stats_page'),
]
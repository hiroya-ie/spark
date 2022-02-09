from django.urls import path

from . import views
from . import kokusai


app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('ajax-number/', views.ajax_number, name='ajax_number'),
    path('ajax-wiki/', views.ajax_wiki, name='ajax_wiki'),
    path('kokusai', kokusai.ajax_kokusai, name = 'ajax_kokusai'),
    path('kokusai', kokusai.kokusai, name = 'kokusai'),
]
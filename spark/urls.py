from django.urls import path

from . import views
from . import view1
from . import view2
from . import view3
from . import view4
from . import view5
from . import view7

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax-number/', views.ajax_number, name='ajax_number'),
    path('view1', view1.view1, name = 'view1'),
    path('view2', view2.view2, name = 'view2'),
    path('view3', view3.view3, name = 'view3'),
    path('view4', view4.view4, name = 'view4'),
    path('view5', view5.view5, name = 'view5'),
    path('view1/ajax-number/', views.ajax_number, name='ajax_number'),
    path('view2/ajax-wiki/', view2.ajax_wiki, name='ajax_wiki'),
    path('view3/ajax-number/', views.ajax_number, name='ajax_number'),
    path('view4/ajax-number/', views.ajax_number, name='ajax_number'),
    path('view5/ajax-number/', views.ajax_number, name='ajax_number'),
    path('ajax-number/', views.ajax_number, name='ajax_number'),
    path('ajax-wiki/', view2.ajax_wiki, name='ajax_wiki'),
    path('ajax-wiki/', view3.ajax_wiki, name='ajax_wiki'),
    path('ajax-wiki/', view4.ajax_wiki, name='ajax_wiki'),
    path('ajax-wiki/', views.ajax_wiki, name='ajax_wiki'),
    path('ajax-wiki/', view5.ajax_wiki, name='ajax_wiki'),
    path('view6', view5.view6, name = 'view6'),
    path('view7', view7.view7, name = 'view7'),
    path('ajax-wiki/', view7.ajax_wiki, name='ajax_wiki'),
    path('view8', view7.view8, name = 'view8'),
]
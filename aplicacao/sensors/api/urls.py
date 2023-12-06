from django.urls import path, include 
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.index, name='index'),
    path('sensors/', views.sensors_list ),
    path('sensors/<int:id>', views.sensors_detail)
]

urlpatterns =  format_suffix_patterns(urlpatterns)

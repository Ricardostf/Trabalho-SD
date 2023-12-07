from django.contrib import admin
from django.urls import path
from sensors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', views.sensors_list),
    path('sensors/<int:id>/', views.sensors_detail),
]

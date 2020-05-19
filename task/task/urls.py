from django.contrib import admin
from django.urls import path
from task.app import views

# define URL paths
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'get_data/',views.get_data),
    path(r'web_app/', views.show_data, name='web_app'),
    path(r'show_data_from_csv/', views.show_data_from_csv, name='show_data_from_csv'),
]

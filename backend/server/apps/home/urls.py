from apps.home.views import index

from django.urls import path

urlpatterns = [
    path(r'', index, name='home_page')
]

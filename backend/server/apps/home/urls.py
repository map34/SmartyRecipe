from django.urls import path
from apps.home.views import index


urlpatterns = [
    path(r'', index, name='home_page')
]

from django.urls import path

from webapp.views import index, about, search

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('search/', search, name='search_results')
]
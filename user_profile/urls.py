
from django.contrib import admin
from django.urls import path, include
from .views import home, add_story
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('add-story/', add_story, name='add-story')
]


urlpatterns += staticfiles_urlpatterns()
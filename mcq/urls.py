from .views import StoryView



from django.urls import path, include


urlpatterns = [
    path('create-story/', StoryView.as_view(), name='create-story')
]
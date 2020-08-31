from .views import StoryView, StoryCreate



from django.urls import path, include


urlpatterns = [
    path('create-story/', StoryView.as_view(), name='create-story'),
    path('create-story/<int:pk>/', StoryView.as_view(), name='create-story'),
    path('create-question/', StoryCreate.as_view()),
]
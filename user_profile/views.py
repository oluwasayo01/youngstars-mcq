from django.shortcuts import render
from mcq.models import Question, Answer, Story

# Create your views here.
def home(request):
    stories = Story.objects.all()
    return render(request, 'user_profile/stories.html', {'stories': stories})

def add_story(request):
    if request.method == 'POST':
        return
    
    return render(request, 'user_profile/add-story.html')

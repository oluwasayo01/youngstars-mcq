from django.shortcuts import render, get_object_or_404
from mcq.models import Question, Answer, Story
from random import shuffle

# Create your views here.
def home(request):
    stories = Story.objects.all()
    return render(request, 'user_profile/stories.html', {'stories': stories})

def story(request, pk):
    all_questions = {}
    try:
        story = Story.objects.get(heading=pk)
        questions = Question.objects.get(story=story)
        questions = shuffle(questions)
        for index, question in enumerate(questions):
            answer_text = []
            answers = Answer.objects.get(question)
            for index, answer in enumerate(answers):
                answer_text.append(answer[f'option_{int(index) + 1}'])
            all_questions[f'question_{int(index) + 1}'] = {
                'question': question.question,
                'answers': answer_text
            }
    except:
        all_questions = {}
    return render(request, 'user_profile/story.html', {'story': story, 'all_questions': all_questions})

def add_story(request, pk=None):
    
    # questions = Quest
    all_questions = {}
    try:
        obj = get_object_or_404(Story, id=pk)
        questions = Question.objects.get(obj)
        questions = shuffle(questions)
        for index, question in enumerate(questions):
            answer_text = []
            answers = Answer.objects.get(question)
            for index, answer in enumerate(answers):
                answer_text.append(answer[f'option_{int(index) + 1}'])
            all_questions[f'question_{int(index) + 1}'] = {
                'question': question.question,
                'answers': answer_text
            }


    except:
        all_questions = {}
        

    return render(request, 'user_profile/add-story.html', {'questions': all_questions})


def instructions(request):
    return render(request, 'user_profile/instructions.html')

def quiz(request, pk):
    return

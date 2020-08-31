from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import StorySerializer, QuestionSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Story, Question, Answer



class StoryView(APIView):
    serializer_class = StorySerializer

    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        # if serializer.is_valid():
        #     user = serializer.save()
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        heading = request.data.get('heading')
        body = request.data.get('body')
        data = {"heading": heading, "body": body}

        serializer = StorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        story = Story.objects.get(id=pk)
        story.delete()
        return Response('Item deleted', status=status.HTTP_200_OK)

class StoryCreate(APIView):
    

    # def get(self, request):
    #     stories = Story.objects.all()
    #     serializer = StorySerializer(stories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

        # if serializer.is_valid():
        #     user = serializer.save()
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        question = request.data.get('question')
        heading = request.data.get('heading')
        option_1 = request.data.get('option_1')
        option_2 = request.data.get('option_2')
        option_3 = request.data.get('option_3')
        option_4 = request.data.get('option_4')
        correct_option = request.data.get('correct_option')
        s = Story.objects.get(heading=heading)
        q = Question(story=s, question=question)
        q.save()
        data = {'question': q.id, "option_1": option_1, "option_2": option_2, "option_3": option_3, "option_4": option_4, "correct_option": correct_option}

        serializer = AnswerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

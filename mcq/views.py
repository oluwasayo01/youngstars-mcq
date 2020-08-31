from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StorySerializer
from rest_framework.response import Response
from rest_framework import status


class StoryView(APIView):
    serializer_class = StorySerializer

    def post(self, request):
        heading = request.data.get('heading')
        body = request.data.get('body')

        data = {"heading": heading, "body": body}

        serializer = StorySerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.

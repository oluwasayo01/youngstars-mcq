from rest_framework.serializers import ModelSerializer
from .models import Story, Answer, Question


class StorySerializer(ModelSerializer):

    class Meta:
        model = Story
        fields = '__all__'
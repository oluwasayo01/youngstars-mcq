from django.db import models

# Create your models here.
class Story(models.Model):
    heading = models.CharField(max_length=50, blank=False, null=False)
    body = models.TextField(blank=False, null=False, editable=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    question = models.TextField(max_length=200, blank=False, null=False)
    options = models.Ch
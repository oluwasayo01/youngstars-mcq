from django.db import models

# Create your models here.
class Story(models.Model):
    heading = models.CharField(max_length=50, blank=False, null=False)
    body = models.TextField(blank=False, null=False, editable=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class Question(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    question = models.TextField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.question

class Answer(models.Model):

    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    option_1 = models.CharField(max_length=50, null=False, blank=False)
    option_2 = models.CharField(max_length=50, null=False, blank=False)
    option_3 = models.CharField(max_length=50, null=False, blank=False)
    option_4 = models.CharField(max_length=50, null=False, blank=False)
    correct_option = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'Options: [{self.option_1}, {self.option_2}, {self.option_3}, {self.option_4}] Correct: {self.correct_option}'

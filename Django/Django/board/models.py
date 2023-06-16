from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    voter = models.ManyToManyField(User, related_name='voter_question')
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey로 Question 속성을 가져가며 CASCADE로 질문이 삭제될 경우 같이 삭제
    content = models.TextField()
    voter = models.ManyToManyField(User, related_name='voter_answer')
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(null=True, blank=True)
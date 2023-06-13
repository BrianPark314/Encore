from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey로 Question 속성을 가져가며 CASCADE로 질문이 삭제될 경우 같이 삭제
    content = models.TextField()
    created_at = models.DateTimeField()
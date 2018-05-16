from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

class Answer(models.Model):
    answer_text = models.CharField(max_length=150)

    def __str__(self):
        return self.answer_text


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    question_text = models.CharField(max_length=150)
    answer = models.OneToOneField('Answer', on_delete=models.CASCADE,
                                  related_name='correct_answer', null=True, blank=True)
    choices = models.ManyToManyField(Answer, related_name='choices')

    def __str__(self):
        return self.question_text


class Quiz(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=150)
    question = models.ManyToManyField(Question, blank=True)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return self.quiz_name

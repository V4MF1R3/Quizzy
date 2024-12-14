from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correct_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])

    def __str__(self):
        return self.question_text[:50]

class QuizSession(models.Model):
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"Session - {self.id}"

class Answer(models.Model):
    session = models.ForeignKey(QuizSession, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.IntegerField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Session {self.session.id} - Question {self.question.id}"
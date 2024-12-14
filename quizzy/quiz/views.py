from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, QuizSession, Answer
import random

def start_quiz(request):
    session = QuizSession.objects.create()
    return redirect('quiz:next_question', session_id=session.id)


def next_question(request, session_id):
    session = get_object_or_404(QuizSession, id=session_id)
    
    answered_questions = session.answers.values_list('question_id', flat=True)
    
    unanswered_questions = Question.objects.exclude(id__in=answered_questions)
    
    if unanswered_questions.exists():
        question = random.choice(unanswered_questions)
        return render(request, 'question.html', {'session': session, 'question': question})
    else:
        return redirect('quiz:results', session_id=session.id)


def submit_answer(request, session_id, question_id):
    session = get_object_or_404(QuizSession, id=session_id)
    question = get_object_or_404(Question, id=question_id)
    
    selected_option = int(request.POST.get('answer'))
    is_correct = selected_option == question.correct_option

    Answer.objects.create(
        session=session,
        question=question,
        selected_option=selected_option,
        is_correct=is_correct,
    )

    session.total_questions += 1
    if is_correct:
        session.correct_answers += 1
    else:
        session.incorrect_answers += 1
    session.save()

    return redirect('quiz:next_question', session_id=session.id)


def results(request, session_id):
    session = QuizSession.objects.get(id=session_id)
    return render(request, 'results.html', {'session': session})

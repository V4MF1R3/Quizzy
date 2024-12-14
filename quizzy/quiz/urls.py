from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    # path('', views.home, name='home'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('<int:session_id>/next/', views.next_question, name='next_question'),
    path('<int:session_id>/<int:question_id>/submit/', views.submit_answer, name='submit_answer'),
    path('<int:session_id>/results/', views.results, name='results'),
]

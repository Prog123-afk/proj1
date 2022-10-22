from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz

# Create your views here.
def index(request):
    quizs = Quiz.objects.all()
    ctx = {'quizs':quizs}
    return render(request, 'quiz/index.html', ctx)

def quiz(request, id):
    qz = Quiz.objects.get(pk=id)
    ques = qz.question_set.all()
    if request.method == 'POST':
        for q in ques:
            ans = request.POST.get(f'q{q.id}').strip().lower()
            if ans != q.ans.strip().lower():
                return HttpResponse('You failed!')
        return HttpResponse('You won')

    ctx = {'qz': qz, 'ques':ques}
    return render(request, 'quiz/quiz.html', ctx)



from django.shortcuts import get_object_or_404, render
from my_app.models import Question
from my_app.models import Choice


def requst_1(request):
    return render(request, 'home.html')


def question_list(request):
    questions = Question.objects.all()
    context = {
        'questions': questions

    }
    return render(request, 'polls/question.html', context=context)


def question_detil(requests, pk):
    questions = get_object_or_404(Question, id=pk)
    choices = Choice.objects.filter(question=questions)
    context = {
        'questions': questions,
        'choices': choices
    }
    return render(requests, 'polls/questioin_detil.html', context=context)

from django.shortcuts import render

def salom(request):
    items = [
        {'field1': 'Value 1', 'field2': 'Value 2', 'field3': 'Value 3'},
        {'field1': 'Value 4', 'field2': 'Value 5', 'field3': 'Value 6'},
        {'field1': 'Value 7', 'field2': 'Value 8', 'field3': 'Value 9'}
    ]
    return render(request, 'salom.html', {'items': items})

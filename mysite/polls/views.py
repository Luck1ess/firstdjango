from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")

def detail(request, question_id):
    return HttpResponse("You are looking at quest %s. " % question_id)

def results(request, question_id):
    response = 'Look %s.'
    return HttpResponse(response % question_id )

def vote(request, question_id):
    return HttpResponse('You vote %s. ' % question_id)


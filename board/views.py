from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.
def index(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
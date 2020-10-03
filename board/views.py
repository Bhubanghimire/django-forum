from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm

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


def new_topics(request, id):

    board = get_object_or_404(Board, pk=id)
    user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            subject = request.POST['subject']
            message = request.POST['message']

            topic = Topic.objects.create(
                subject=subject,
                board=board,
                starter=user
            )

            post = Post.objects.create(
                message=message,
                topic=topic,
                created_by=user
            )

            # TODO: redirect to the created topic page
            return redirect('board_topics', id=board.id)

    else:
        form = NewTopicForm()
    return render(request, 'new_topics.html', {'board': board,'form':form})

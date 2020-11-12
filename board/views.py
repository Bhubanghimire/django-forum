from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, FormView, UpdateView, CreateView

# Create your views here.
from .models import Topic


def index(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

@login_required
def board_topics(request, pk):
    board = get_object_or_404(Board,pk=pk)
    return render(request, 'topics.html', {'board': board})

@login_required
def new_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first() 
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.starter = request.user 
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user  
            )
            return redirect('board_topics', pk=board.pk) 
    else:
        form = NewTopicForm()
    return render(request, 'new_topics.html', {'board': board, 'form': form})



class TopicPostsView(DetailView):
    model = Topic
    template_name = "topic_posts.html"

    def get_object(self):
        self.topic = get_object_or_404(
            Topic, board__pk=self.kwargs['pk'], pk=self.kwargs['topic_pk'])
        
        return self.topic

    def get_context_data(self, **kwargs):
        session_key = 'viewed_topic_{}'.format(self.topic.pk) # <-- here
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True           # <-- until here
        return super().get_context_data(**kwargs)
from django.urls import path
from .views import index,board_topics,new_topics
from .views import TopicPostsView

urlpatterns = [
    path('',index,name='index'),
    path('boards/<int:pk>/', board_topics, name='board_topics'),
    path('boards/<int:pk>/new', new_topics, name='new_topics'),
    # path('boards/<int:pk>/topics/<int:topic_pk>/', topic_posts, name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/',TopicPostsView.as_view(), name="TopicPosts"),

]
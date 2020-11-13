from django.urls import path
from .views import index,board_topics,new_topics,reply_topic,PostUpdateView,UserUpdateView,PostListView
from django.conf.urls import url

urlpatterns = [
    path('',index,name='index'),
    path('boards/<int:pk>/', board_topics, name='board_topics'),
    path('boards/<int:pk>/new', new_topics, name='new_topics'),
    path('boards/<int:pk>/topics/<int:topic_pk>/', PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', reply_topic, name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',PostUpdateView.as_view(), name='edit_post'),
    path('settings/account/', UserUpdateView.as_view(), name='my_account'),


]
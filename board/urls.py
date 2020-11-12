from django.urls import path
from .views import index,board_topics,new_topics,topic_posts
from django.conf.urls import url

urlpatterns = [
    path('',index,name='index'),
    path('boards/<int:pk>/', board_topics, name='board_topics'),
    path('boards/<int:pk>/new', new_topics, name='new_topics'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', topic_posts, name='topic_posts'),

]
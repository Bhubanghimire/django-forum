from django.urls import path
from .views import index,board_topics

urlpatterns = [
    path('',index,name='index'),
    path('boards/<int:id>/', board_topics, name='board_topics'),
]
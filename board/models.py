from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_topic_count(self):
        return Topic.objects.filter(topic__board=self).count()

    
    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=200)
    last_update = models.DateField(auto_now_add=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE,related_name='topic')
    starter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    last_updated = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return self.subject

  


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.message
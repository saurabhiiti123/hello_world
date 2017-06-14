import datetime

from django.db import models

from django.utils import timezone


# Create your models here.
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
          return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
"""
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
"""
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
          return self.choice_text
"""
import datetime
from django.contrib.auth.models import User

from django.db import models

from django.utils import timezone

#models here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    
class Question(models.Model):
    question_title = models.CharField(max_length=300)
    date_created = models.DateTimeField('date published')
    q_id = models.IntegerField(default=0)
    #date_updated = models.DateTimeField('date updated')
    #user_id = models.IntegerField(default=0)
    is_anonymous = models.IntegerField(default=0)
    q_upvote = models.IntegerField(default=0)
    q_downvote = models.IntegerField(default=0)
    description = models.CharField(max_length=100)


class Answer(models.Model):
    answer_text= models.CharField(max_length=500)
    date_answered = models.DateTimeField('date published')
    #que_id = models.IntegerField()
    #date_updated = models.DateTime()
    # user_id = models.IntegerField()
    is_anonymous = models.IntegerField(default=0)
    a_upvote = models.IntegerField(default=0)
    a_downvote = models.IntegerField(default=0)
    def __str__(self):
          return self.answer_text
"""

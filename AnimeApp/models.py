
from django.db import models

# Create your models here.
class Topicinfo(models.Model):
    TopicId=models.AutoField(primary_key=True)
    anime=models.TextField(max_length=500)
    character=models.TextField(max_length=500)
    quote=models.TextField()
    #Date_time=models.DateTimeField()
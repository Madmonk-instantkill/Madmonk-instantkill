from rest_framework import serializers
from AnimeApp.models import Topicinfo

class TopicinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Topicinfo
        fields=('TopicId','anime','character',"quote")

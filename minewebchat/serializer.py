# coding: utf-8
from rest_framework import serializers
from .models import *

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdaChatLog
        fields = ('name','chat')
from django.shortcuts import render
from django.views.generic import ListView
from . models import Message


class MessagesListView(ListView):
    model = Message
    template_name = 'chat/index.html'
    context_object_name = 'messages'

    class Meta:
        ordering = ['-id']
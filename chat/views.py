from django.shortcuts import render

# Create your views here.


def get_chat_view(request):
    template = 'chat_message.html'
    return render(request,template)
# _*_ coding: utf_8 _*_
from django.shortcuts import render

from .models import UserMessage

# Create your views here.
def getform(request):

    #all_message = UserMessage.objects.filter(name='bobby', address='北京')
    #for message in all_message:
    #   print message.name
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('name', '')
        adress = request.POST.get('adress', '')
        email = request.POST.get('email', '')

        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = adress
        user_message.email = email
        user_message.object_id = "helloworld3"

        user_message.save()

    return render(request, 'message_form.html')


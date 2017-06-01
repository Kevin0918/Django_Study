from django.shortcuts import render

# Create your views here.
def getform(requests):
    return render(requests, 'messqge_form.html')

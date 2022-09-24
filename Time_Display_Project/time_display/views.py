from email.utils import localtime
from django.shortcuts import render
from time import localtime, strftime

# Create your views here.
def show(request):
    context = {
        'title': 'Date and Time',
        'date': strftime("%b %d, %Y", localtime()),
        'time': strftime("%I:%M %p", localtime()),
    }
    return render(request, 'index.html', context)
from django.shortcuts import render
from modelform.forms import Majina


def home(request):
    jina = Majina()
    return render(request, 'index.html',{'form':jina})

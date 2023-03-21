from django.shortcuts import render
#from django.http import HttpResponse
from practicaltest.models import Page

def index(request):
    context_dict= {}
    context_dict['list'] = Page.objects.order_by('-date')
    return render(request, 'practicaltest/index.html', context=context_dict)
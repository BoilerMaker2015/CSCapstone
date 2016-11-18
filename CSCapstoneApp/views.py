"""CSCapstone Views

Created by Harris Christiansen on 9/18/16.
"""
from django.shortcuts import render
from django.http import HttpResponse

def getIndex(request):
	return render(request, 'index.html', {
        'foo': 'bar',
    })

def getTable(request):
	return render(request, 'table.html')

def getForm(request):
	return render(request, 'form.html')

def getWelcome(request):
	return render(request,'welcomepage.html')
	#return HttpResponse("sadsadsa")
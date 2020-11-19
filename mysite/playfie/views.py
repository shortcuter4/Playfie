from django.shortcuts import render

from django.http import HttpResponse

# view functions below

# @shortcuter4
# creating a homepage view here that is going to handle the traffic
# from the home page of the news 

def index(request):
	return HttpResponse('<h1>News Home</h1>')

def politics(request):
	return HttpResponse('<h1>News Politics</h1>')

def culture(request):
	return HttpResponse('<h1>News Culture</h1>')

def sport(request):
	return HttpResponse('<h1>News Sport</h1>')

def tourism(request):
	return HttpResponse('<h1>News Tourism</h1>')

def economy(request):
	return HttpResponse('<h1>News Economy</h1>')

'''
def index(request):
	return render(request, 'news/index.html')
'''

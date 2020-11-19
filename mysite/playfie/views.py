from django.shortcuts import render

from django.http import HttpResponse

# view functions below

# @shortcuter4
# creating a homepage view here that is going to handle the traffic
# from the home page of the news 

def index(request):
	return HttpResponse('<h1> Playfie Home</h1>')

'''
def index(request):
	return render(request, 'news/index.html')
'''

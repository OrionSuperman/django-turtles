from django.http import HttpResponse, Http404
from django.shortcuts import render # inserted this line

group = {
	'turtles': [
	{'color' : 'red', 'monkey' : '/static/images/raf.jpg'},
	{'color' :'blue', 'monkey' : '/static/images/leo.jpg'},
	{'color' :'purple', 'monkey' : '/static/images/don.jpg'},
	{'color' :'orange', 'monkey' : '/static/images/mic.jpg'}
	]
}

def index(request):
	turtles = group
	return render(request, 'turtles/index.html', turtles) # updated this line

def color(request, color):
	print color
	turtles = None
	for each in group['turtles']:
		if each['color'] == color:
			turtles ={'turtles' : [
			each
			]
			}

	if not turtles:
		turtles ={
		'turtles' : [ 
			{'color' : 'kinda yucky', 'monkey' : '/static/images/apr.jpg'}
			]
		}

	return render(request, 'turtles/index.html', turtles)
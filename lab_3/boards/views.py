from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
from django.contrib import admin
from .models import Board 
# Import the views from our boards app
from boards import views
 

# Create your views here.
def home(request):
	return HttpResponse('Welcome to the discussion board!')

#define a method home which will get a list of board names from our database
def home(request):
	boards = Board.objects.all()
	boards_names = list()

	for board in boards:
		boards_names.append(board.name)

	response_html = '<br>'.join(boards_names)

	return HttpResponse(response_html)

def home(request):
	boards = Board.objects.all()
	return render(request, 'home.html', {'boards': boards})


#add a pattern so that if no specific request is made we route to the home method in our views.py of boards
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^admin/', admin.site.urls),
]

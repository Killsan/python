from django.shortcuts import render
# FUCK THIS FUCKING FRAMEWORK
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Fuck django")
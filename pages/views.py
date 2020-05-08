from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/landing.html')

def target(request):
	return render(request,'pages/where_money_goes.html')
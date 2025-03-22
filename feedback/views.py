from django.shortcuts import render,HttpResponse

# Create your views here.
def feedback(request):
    return HttpResponse("This is Feddback Page")

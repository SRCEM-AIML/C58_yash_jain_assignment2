from django.shortcuts import render,HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("This is home page")

def index(request):
    context = {
    "var1" :"Yash",
    "var2" :"Jain"
    }
    return render(request, 'index.html',context)
def about(request):
    return HttpResponse("This is about page")
from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    context = {
        "Variable1": "Harry is Great",
        "Variable2": "Rohan is Great"
        }
    return render(request,'index.html',context)
    # return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is about")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is Contact page")
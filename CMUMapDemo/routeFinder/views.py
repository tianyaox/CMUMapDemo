from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"routeFinder/index.html",{})

def demo2(request):
    return render(request,"routeFinder/demo2.html",{})
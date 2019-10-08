from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"base.html")

def django(request):
    return render(request,"django.html")

def templates(request):
    return render(request,"templates.html")
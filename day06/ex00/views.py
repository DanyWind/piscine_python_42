from django.shortcuts import render

# Create your views here.
def home(request):
    user = "Daniel"
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'base.html', locals())
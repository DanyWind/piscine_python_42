from django.shortcuts import render
from ex02.forms import ContactForm

# Create your views here.
def form(request):

    form = ContactForm(request.POST or None)

    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'form.html', locals())
from django.shortcuts import render

def create_couleurs(n_rows):
    rows = []
    for i in range(n_rows):
        couleurs = [
            f"rgba(0,0,0,{float(i) / n_rows})",
            f"rgba(255,0,0,{float(i) / n_rows})",
            f"rgba(0,255,0,{float(i) / n_rows})",
            f"rgba(0,0,255,{float(i) / n_rows})"
        ]
        rows.append(couleurs)
    return rows

# Create your views here.
def table(request):
    n_rows = 50
    rows = create_couleurs(n_rows)

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'table.html', locals())
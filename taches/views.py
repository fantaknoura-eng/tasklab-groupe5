from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tache
from .forms import TacheForm

def liste_taches(request):
    statut = request.GET.get("statut", "")
    if statut not in dict(Tache.STATUTS):
        statut = ""
    priorite_1 = request.GET.get("priorite") == "1"
    taches = Tache.objects.all().order_by("-date_creation")
    if statut:
        taches = taches.filter(statut=statut)
    if priorite_1:
        taches = taches.filter(priorite=1)
    return render(
        request,
        "taches/liste.html",
        {
            "taches": taches,
            "statuts": [
                (code, libelle, "selected" if code == statut else "")
                for code, libelle in Tache.STATUTS
            ],
            "statut_selectionne": statut,
            "priorite_1_checked": "checked" if priorite_1 else "",
        },
    )

def creer_tache(request):
    form = TacheForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        tache = form.save()
        messages.success(request, f"La tâche « {tache.titre} » a été créée.")
        return redirect("liste_taches")
    return render(request, "taches/form.html", {"form": form, "titre": "Nouvelle tâche"})

def modifier_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    form = TacheForm(
        request.POST if request.method == "POST" else None,
        instance=tache,
    )
    if request.method == "POST" and form.is_valid():
        tache = form.save()
        messages.success(request, f"La tâche « {tache.titre} » a été modifiée.")
        return redirect("liste_taches")
    return render(request, "taches/form.html", {"form": form, "titre": "Modifier la tâche"})

@require_POST
def supprimer_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    titre = tache.titre
    tache.delete()
    messages.success(request, f"La tâche « {titre} » a été supprimée.")
    return redirect("liste_taches")

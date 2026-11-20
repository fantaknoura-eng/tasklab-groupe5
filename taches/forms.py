from django import forms
from .models import Tache


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ["titre", "description", "statut", "priorite"]
        widgets = {
            "titre": forms.TextInput(attrs={"placeholder": "Titre de la tâche"}),
            "description": forms.Textarea(attrs={"rows": 3, "placeholder": "Description (optionnelle)"}),
            "priorite": forms.NumberInput(attrs={"min": 1, "max": 3}),
        }

    def clean_titre(self):
        titre = self.cleaned_data.get("titre", "").strip()
        if not titre:
            raise forms.ValidationError("Le titre ne peut pas être vide.")
        return titre

    def clean_priorite(self):
        priorite = self.cleaned_data["priorite"]
        if not 1 <= priorite <= 3:
            raise forms.ValidationError("La priorité doit être entre 1 et 3.")
        return priorite

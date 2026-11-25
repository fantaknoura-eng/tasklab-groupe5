from django.test import TestCase
from django.urls import reverse
from .models import Tache
from .forms import TacheForm

class TacheTests(TestCase):
    def test_creation_modele(self):
        tache = Tache.objects.create(titre="Réviser Django")
        self.assertEqual(str(tache), "Réviser Django")

    def test_formulaire_creation_valide(self):
        form = TacheForm(
            data={
                "titre": "Préparer le TP2",
                "description": "Écrire les tests Django",
                "statut": "A_FAIRE",
                "priorite": 2,
            }
        )

        self.assertTrue(form.is_valid(), form.errors)
        tache = form.save()
        self.assertEqual(Tache.objects.get(pk=tache.pk).titre, "Préparer le TP2")

    def test_liste_accessible(self):
        response = self.client.get(reverse("liste_taches"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taches/liste.html")

    def test_creation_par_post(self):
        response = self.client.post(
            reverse("creer_tache"),
            {
                "titre": "Créer une tâche",
                "description": "Création depuis le formulaire",
                "statut": "A_FAIRE",
                "priorite": 2,
            },
        )

        self.assertRedirects(response, reverse("liste_taches"))
        self.assertTrue(Tache.objects.filter(titre="Créer une tâche").exists())

    def test_suppression_par_post(self):
        tache = Tache.objects.create(titre="Tâche à supprimer")

        response = self.client.post(
            reverse("supprimer_tache", args=[tache.pk])
        )

        self.assertRedirects(response, reverse("liste_taches"))
        self.assertFalse(Tache.objects.filter(pk=tache.pk).exists())

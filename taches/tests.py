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

    def test_liste_filtre_par_statut(self):
        Tache.objects.create(titre="À faire")
        en_cours = Tache.objects.create(titre="En cours", statut="EN_COURS")

        response = self.client.get(
            reverse("liste_taches"), {"statut": "EN_COURS"}
        )

        self.assertEqual(
            list(response.context["taches"].values_list("pk", flat=True)),
            [en_cours.pk],
        )

    def test_liste_filtre_priorite_1(self):
        priorite_1 = Tache.objects.create(titre="Urgente", priorite=1)
        Tache.objects.create(titre="Normale", priorite=2)

        response = self.client.get(reverse("liste_taches"), {"priorite": "1"})

        self.assertEqual(
            list(response.context["taches"].values_list("pk", flat=True)),
            [priorite_1.pk],
        )

    def test_filtres_statut_et_priorite_sont_combinables(self):
        correspondante = Tache.objects.create(
            titre="Urgente en cours", statut="EN_COURS", priorite=1
        )
        Tache.objects.create(titre="Urgente terminée", statut="TERMINEE", priorite=1)
        Tache.objects.create(titre="Normale en cours", statut="EN_COURS", priorite=2)

        response = self.client.get(
            reverse("liste_taches"),
            {"statut": "EN_COURS", "priorite": "1"},
        )

        self.assertEqual(
            list(response.context["taches"].values_list("pk", flat=True)),
            [correspondante.pk],
        )

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

    def test_creation_par_post_vide_affiche_erreurs(self):
        response = self.client.post(reverse("creer_tache"), data={})

        self.assertEqual(response.status_code, 200)
        self.assertIn("titre", response.context["form"].errors)
        self.assertFalse(Tache.objects.exists())

    def test_modification_par_post_vide_affiche_erreurs(self):
        tache = Tache.objects.create(titre="Tâche existante")

        response = self.client.post(
            reverse("modifier_tache", args=[tache.pk]), data={}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("titre", response.context["form"].errors)
        tache.refresh_from_db()
        self.assertEqual(tache.titre, "Tâche existante")

    def test_suppression_par_post(self):
        tache = Tache.objects.create(titre="Tâche à supprimer")

        response = self.client.post(
            reverse("supprimer_tache", args=[tache.pk])
        )

        self.assertRedirects(response, reverse("liste_taches"))
        self.assertFalse(Tache.objects.filter(pk=tache.pk).exists())

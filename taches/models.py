from django.db import models

class Tache(models.Model):
    STATUTS = [
        ("A_FAIRE", "À faire"),
        ("EN_COURS", "En cours"),
        ("TERMINEE", "Terminée"),
    ]
    PRIORITES = [
        (1, "Basse"),
        (2, "Normale"),
        (3, "Haute"),
    ]
    titre = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    statut = models.CharField(max_length=12, choices=STATUTS, default="A_FAIRE")
    priorite = models.PositiveSmallIntegerField(choices=PRIORITES, default=2)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(priorite__in=[1, 2, 3]),
                name="tache_priorite_valide",
            ),
        ]

    def __str__(self):
        return self.titre

# Notes de version

## v1.1.0 — 2026-11-25

- Corrige la validation des soumissions POST vides pour les formulaires de création et de modification.
- Ajoute le filtre de tâches par statut.
- Ajoute le filtre de priorité 1 du groupe 5, combinable avec le filtre par statut.
- Ajoute les tests de régression et de filtrage associés.

## v1.0.0 — 2026-11-25

Première version stable de TaskLab.

- Gestion des tâches : création, consultation, modification et suppression.
- Validation du titre et des priorités autorisées.
- Contraintes de priorité appliquées au modèle et à la base de données.
- Interface responsive et confirmations après les opérations CRUD.
- Configuration locale par variables d’environnement et fichier `.env`.
- Tests Django et workflow CI GitHub Actions.
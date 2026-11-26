# Bilan final — TaskLab Groupe 5

## Travail accompli

- Application Django de gestion de tâches : création, consultation, modification et suppression.
- Validation du titre et des priorités, avec contrainte de priorité au niveau de la base.
- Interface responsive et messages de confirmation après les opérations.
- Configuration locale documentée avec `.env`, dépendances et migrations versionnées.
- TP2 : tests de création valide, GET de liste, création par POST et suppression par POST. Un défaut temporaire de validation a été introduit, détecté par test, puis corrigé.
- TP4 : correction des formulaires soumis par POST vide; filtres combinables par statut et priorité 1, variante du groupe 5.
- Pull requests fusionnées dans `main`; tags `v1.0.0` et `v1.1.0` publiés.

## Vérifications

- `python manage.py test` : 10 tests réussis.
- `python manage.py makemigrations --check --dry-run` : aucune migration manquante.
- GitHub Actions sur `main` : succès après la fusion TP4.

## Suivi du projet

- Les six membres du groupe 5 ont participé à la répartition, au suivi et à la validation du travail : #8, #10, #11, #12, #13 et #14.
- Les Pull Requests ont fait l’objet d’une relecture par un autre membre du groupe avant leur fusion dans `main`.
- L’issue #8 a été corrigée par la PR #9 et clôturée après validation.
- Le tableau Trello [TaskLab Groupe 5 — TP Génie Logiciel](https://trello.com/b/cuS87Krg/tasklab-groupe-5-tp-g%C3%A9nie-logiciel) a été créé avec les listes « À faire », « En cours » et « Terminé ».

## Écarts et incidents

- Un POST vide de création/modification rendait le formulaire non lié et masquait les erreurs. Le défaut a été reproduit, testé, corrigé et intégré.
- Le serveur local a nécessité l’application de la migration de priorité avant l’ouverture de la page.
- La difficulté principale a été la coordination de l’ensemble des livrables Git/GitHub, qui a été résolue par la répartition des tâches, les validations croisées et la mise à jour régulière du dépôt.

## Améliorations futures

- Recherche par mot-clé dans les tâches.
- Tri des tâches et pagination.
- Confirmation avant suppression.
- Préparation et vérification d’un déploiement Django de production.
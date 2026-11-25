# TaskLab TWIN2 — Groupe 5

Application Django de gestion de tâches, réalisée pour le TP fil rouge de Génie Logiciel.

## Prérequis

- Python 3.11 ou supérieur
- Git

## Installation

```bash
git clone https://github.com/fantaknoura-eng/tasklab-groupe5.git
cd tasklab-groupe5
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Sous Windows PowerShell, active l’environnement avec `.venv\\Scripts\\Activate.ps1` et copie la configuration avec `Copy-Item .env.example .env`.

L’application est ensuite disponible sur http://127.0.0.1:8000/.

## Configuration

Les paramètres locaux sont lus depuis `.env` à la racine du dépôt. `.env.example` est le modèle à copier; les valeurs locales et les secrets ne doivent pas être commités.

| Variable | Description | Exemple local |
| --- | --- | --- |
| `DEBUG` | Active le mode debug Django | `True` |
| `SECRET_KEY` | Clé secrète Django | Générer une valeur aléatoire pour chaque environnement |
| `ALLOWED_HOSTS` | Hôtes autorisés, séparés par des virgules | `127.0.0.1,localhost` |

`.env`, `.venv/` et `db.sqlite3` sont exclus par `.gitignore` : le premier contient une configuration locale potentiellement sensible, le deuxième contient les dépendances installées sur une machine et la base SQLite contient des données locales. Seul `.env.example`, sans secret réel, est versionné.

## Migrations et tests

Les migrations existantes sont versionnées. Pour initialiser la base, applique-les avec `python manage.py migrate`. Après une modification de modèle, crée une migration avec `python manage.py makemigrations taches`, puis vérifie-la avec `python manage.py makemigrations --check --dry-run`.

Exécute les tests avec :

```bash
python manage.py test
```

## Version

La note de version de `v1.0.0` est disponible dans [CHANGELOG.md](CHANGELOG.md).

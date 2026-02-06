# WATER

## Présentation

Water est une application de suivi de consommation d'eau.

A chaque clic, cela signifie qu'un verre d'eau a été consommé.
Les informations sont sauvegardées dans un fichier au format JSON.
Il est possible de fournir un récapitulatif par jour de la consommation d'eau.
A la mi journée, il faut une alerte si le seuil minimal n'est pas atteint à 50%.

## Compilation

Environnement Python 3.11 minimum

### Local

Pour préparer l'environnement, vous devez créer un environnement virtuel et l'activer

```bash
python -m venv .venv
source ./.venv/bin/activate
```

Pour lancer les tests et l'analyse de couverture de code, utilisez le script suivant.

```bash
pip install -f requirements.txt
coverage run -m pytest testapp.py
#FIXME
```

### Environnement Docker

Pour lancer les tests et l'analyse de couverture de code au format XML, sans avoir besoin de créer un environnement virtuel directement, reprenez la commande ci-après en remplaçant le chemin HOME_PROJECT/project-tofix par le chemin absolu vers le projet.

```bash
#FIXME
```


Envoyer l'analyse de code à une instance SonarQube en local.

```bash
#FIXME
```

## Utilisation

Pour utiliser et tester en situation nominale le service, utilisez les commandes suivantes.

```bash
python -m venv .venv
. ./.venv/bin/activate
pip install -f requirements.txt
python app.py
```

Si l'application ne démarre pas correctement, ajouter le fichier json à la racine de votre application.

```json
{"water": 0}
```

## Evolution alerte

Plutôt que chaque client vérifie si une alerte doit être déclenchée à la mi-journée, faites-en sorte d'enregistrer la liste des clients à contacter en cas de trop faible quantité d'eau consommée.

La notification d'un client sera seulement une simulation vous devez donc afficher le message suivant dans un fichier de log appelé `notification.log`.

```
Alerte, manque d'eau pour le profile XXXX
```


## POO

Refactoriser l'application pour regrouper les différentes parties/fonctionnalités au sein de classes afin de ne plus avoir de simples fonctions appelées directement dans les points d'accès.


## Résumé des modifications

1. Tester l'application pour faire fonctionner les éléments de base
2. Absorber la dette technique en sélectionnant les actions rapides
3. Refactoriser le code en suivant les principes de la POO

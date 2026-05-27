# Analyses

![](./schema.drawio.png)

## Démarrage du serveur SonarQube

Via un conteneur docker en mode standalone en suivant la documentation et les prérequis.

```bash
docker run --name sonarqube-test -d -p 9000:9000 sonarqube:latest
```

## Déclencher une analyse statique

Créer le projet dans SonarQube.

Créer un token d'accès à SonarQube.

### SonarScanner CLI

Créer un sous-réseau docker

```bash
docker network create sonar_network
```

Rattacher le conteneur sonarqube en lui associant un alias réseau

```bash
docker network connect sonar_network sonarqube-test --alias sonarqube
```

Déclencher l'analyse statique et soumettre le résultat au serveur SonarQube.

```bash
YOUR_REPO="."
SONARQUBE_URL="sonarqube:9000"
docker run --rm -e SONAR_HOST_URL="http://${SONARQUBE_URL}" -e SONAR_TOKEN="sqp_f3c63a7e16444d5997c134bd924260c5c36308b7" --network sonar_network -v "${YOUR_REPO}:/usr/src" sonarsource/sonar-scanner-cli
```

### SonarScanner for Python
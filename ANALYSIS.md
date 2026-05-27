# Analyses

![](./schema.drawio.png)

## Démarrage du serveur SonarQube

Via un conteneur docker en mode standalone en suivant la documentation et les prérequis.

```bash
docker run --name sonarqube-test -d -p 9000:9000 sonarqube:latest
```

Attendre que le message `SonarQube is operational` dans les logs

```bash
docker logs sonarqube-test
```

## Déclencher une analyse statique

Créer le projet dans SonarQube et enregister le nom dans le fichier de configuration `sonar-project.properties`

```properties
sonar.projectKey=webapp
```

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
docker run --rm -e SONAR_HOST_URL="http://${SONARQUBE_URL}" -e SONAR_TOKEN="<$your_sonar_token>" --network sonar_network -v "${YOUR_REPO}:/usr/src" sonarsource/sonar-scanner-cli
```

### SonarScanner for Python
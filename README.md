# ift215-projet
Projet sur la santé mentale dans le cadre du cours IFT215: interface et multimédia

## Développement

Pour démarrer le projet faire:
```
docker compose up --build
```

Pour faire un healthcheck aller sur la page `http://localhost:8080/ping`

## Routes

| Route | Méthode | Description |
| --- | --- | --- |
| `/ping` | GET | Vérifie si le serveur est en ligne |
| `/login` | POST<br />GET | Permet de se connecter<br />Affiche la page de connexion |
| `/register` | POST<br />GET | Permet de s'inscrire<br />Affiche la page d'inscription |
| `/logout` | GET | Permet de se déconnecter |
| `/me` | GET | Affiche les informations de l'utilisateur connecté |

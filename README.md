# ift215-projet
Projet sur la santé mentale dans le cadre du cours IFT215: interface et multimédia

## Développement

Pour démarrer le projet faire:
```
docker compose up --build
```

Pour faire un healthcheck aller sur la page `http://localhost:8080/ping`

## Routes

| Route                             | Méthode | Description                                                                  | exemple payload                          |
|-----------------------------------|---------|------------------------------------------------------------------------------|------------------------------------------|
| **HEALTHCHECK**                   |         |                                                                              |                                          |
| `/ping`                           | GET     | Vérifie si le serveur est en ligne                                           | `NAN`                                    |
| **AUTHENTIFICATION**              |         |                                                                              |                                          |
| `/login`                          | GET     | Affiche la page de connexion                                                 | `NAN`                                    |
| `/register`                       | GET     | Affiche la page d'inscription                                                | `NAN`                                    |
| `/login`                          | POST    | Permet de se connecter                                                       | ```{ "username": "", "password": "" }``` |
| `/register`                       | POST    | Permet de s'inscrire                                                         | ```{ "username": "", "password": "" }``` |
| `/logout`                         | GET     | Permet de se déconnecter                                                     | `NAN`                                    |
| `/me`                             | GET     | Affiche les informations de l'utilisateur connecté                           | `NAN`                                    |
| **CALENDRIER DES ÉMOTIONS**       |         |                                                                              |                                          |
| `/emotions/:start_date/:end_date` | GET     | Liste les émotions pour l'utilisateur connecté sur la période de temps ciblé | `NAN`                                    |
| `/emotion`                        | POST    | Ajoute une émotion pour l'utilisateur connecté                               | ```{ "emotion": "", "date": "" }```      |
| `/emotion`                        | DELETE  | Supprime une émotion pour l'utilisateur connecté                             | ```{ "id": 0 }```                        |

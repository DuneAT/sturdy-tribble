# sturdy-tribble (but it's DeepGaze applied to carttons)

## DeepGaze IIE pour le calcul de saillance en situation d'image non réaliste

### Principe d'utilisation et source

Ce notebook est construit à partir du notebook déposé sur le repo GitHub DeepGaze, et disponible à l'adresse : https://github.com/matthias-k/DeepGaze/tree/main

L'objectif est de tester la robustesse et la vitesse d'exécution du modèle générique pré-entraîné sur des images de type photoréaliste, face à des images simplifiées de types "Cartoon". 

(rajouter source de données de test, lien du papier : à venir)

### Méthode de comparaison des résultats avec le modèle KSDG20 employé actuellement

Chaque modèle est tout d'abord comparé avec l'observation expérimentale du regard utilisateur confronté à la scène dont les frames sont utilisées ici pour l'évaluation. On observe dansd un premier temps si une intersection existe entre la saillance calculée d'une frame et le regard de l'utilisateur sur une plage de 1 seconde (fréquence de rafraichissement du modèle vis à vis du mouvement de la vidéo). Si cette intersection est non vide, alors le modèle a deviné juste (précision = 1), sinon il a faux (précision = 0). Cette méthode de comparaison sera revue plus tard, et ajustée en réponse à des comportements détaillés dans la suite de l'étude.

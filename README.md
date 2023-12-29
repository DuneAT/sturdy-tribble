# sturdy-tribble (but it's DeepGaze applied to cartoons)

see https://github.com/matthias-k/DeepGaze/tree/main for original repo :)

## DeepGaze IIE pour le calcul de saillance en situation d'image non réaliste

### Principe d'utilisation et source

Ce notebook est construit à partir du notebook déposé sur le repo GitHub DeepGaze, et disponible à l'adresse : https://github.com/matthias-k/DeepGaze/tree/main

L'objectif est de tester la robustesse et la vitesse d'exécution du modèle générique pré-entraîné sur des images de type photoréaliste, face à des images simplifiées de types "Cartoon". 

(rajouter source de données de test, lien du papier : à venir)

### Méthode de comparaison des résultats avec le modèle KSDG20 employé actuellement

Chaque modèle est tout d'abord comparé avec l'observation expérimentale du regard utilisateur confronté à la scène dont les frames sont utilisées ici pour l'évaluation. On observe dansd un premier temps si une intersection existe entre la saillance calculée d'une frame et le regard de l'utilisateur sur une plage de 1 seconde (fréquence de rafraichissement du modèle vis à vis du mouvement de la vidéo). Si cette intersection est non vide, alors le modèle a deviné juste (précision = 1), sinon il a faux (précision = 0). Cette méthode de comparaison sera revue plus tard, et ajustée en réponse à des comportements détaillés dans la suite de l'étude.

### Nouvelle méthode implémentée : temps fixe

On décide pour une approche plus précise de considérer de nouvelles évaluations basées sur les indicateurs suivants.

#### Couverture

La couverture E1 est un indicateur de la bonne couverture du regard d'un utilisateur, pour un instant précis, par la carte de saillance prédite par le modèle. Dans le cas d'une prédiction parfaite, cet indicateur vaut 1.

#### Malprédiction du regard

La malprédiction E2 est un indicateur de l'existence d'une intensité non nulle du regard à un endroit dont la carte de saillance présente une valeur nulle. Dans le cas d'une prédiction parfaite, cet indicateur vaut 0.

#### Saillance superflue

La saillance superflue E3 est un indicateur de l'existence d'une intensité nulle du regard à un endroit dont la carte de saillance présente une valeur non nulle. Dans le cas d'une prédiction parfaite, cet indicateur vaut 0.


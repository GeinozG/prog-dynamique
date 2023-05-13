# Tester le programme

Le programme a été conçu et testé sous Windows 11 uniquement. De ce fait, toutes les démarches pour tester le projet ne seront compatibles qu'avec un système d'exploitation Windows.

## Télécharger et tester l'exécutable

Une version du programme déjà compilé sous Windows 11 est disponible dans le dépôt Github suivant : "https://github.com/GeinozG/travail-perso-minimax/releases/tag/v1.0.0". Une fois le dossier téléchargé, il suffit de le décompresser et d'exécuter le programme *connect4_minimax.exe*.

Il est possible de changer la profondeur de recherche, le joueur qui a l'initiative et la taille de la fenêtre dans le fichier *config.txt* qui se trouve dans le même répertoire que l'exécutable.

## Compiler le programme

La façon la plus simple et rapide de compiler le programme est avec MinGW-w64. Il s'agit d'un compilateur en ligne de commande très simple d'utilisation. Après avoir téléchargé ce compilateur, il faut cloner le dépôt Github suivant : "https://github.com/GeinozG/travail-perso-minimax". Ensuite, il faut soit exécuter la ligne de commande qui se trouve dans le fichier "Makefile", à la racine du dossier du projet, soit exécuter directement la commande `make` dans le dossier où se trouve le fichier "Makefile". Dans le dernier cas, il faut que Make soit installé.

## Comment jouer

Il s'agit d'un jeu Puissance 4. Les règles sont simples, le premier joueur à aligner quatre jetons de sa couleur gagne la partie. Chaque jeton est soumis à une gravité verticale, c'est-à-dire qu'aucun jeton ne peut flotter, ils s'alignent pour former des colonnes. Enfin, pour poser un jeton, il suffit d'effectuer un clic gauche avec la souris dans la colonne désirée.
# Tester le programme

Le programme a été conçu et testé sous Windows 11 uniquement. De ce fait, toutes les démarches pour tester le projet ne seront compatibles qu'avec un système d'exploitation Windows.

## Télécharger et tester l'exécutable

Une version du programme déjà compilé sous Windows 11 est disponible dans le dépôt Github suivant : [https://github.com/GeinozG/minimax-connect4/releases/...](https://github.com/GeinozG/minimax-connect4/releases/...). Une fois le dossier téléchargé, il suffit de le décompresser et d'exécuter le programme *connect4_minimax.exe*.

Il est possible de changer la profondeur de recherche et le joueur qui à l'initiative et la taille de la fenêtre dans le fichier *config.txt* qui se trouve dans le même répertoire que l'exécutable.

## Compiler le programme

La façon la plus simple et rapide pour compiler le programme est avec Visual Studio Code.

## Comment jouer

Il s'agit d'un jeu Puissance 4. Les règles sont simples, le premier joueur à aligner quatre jetons de sa couleur gagne la partie. Chaque jeton est soumis à une gravité verticale, c'est-à-dire qu'aucun jeton ne peut flotter, ils s'alignent pour former des colonnes. Enfin, pour poser un jeton, il suffit d'effectuer un clic gauche avec la souris dans la colonne désirée.
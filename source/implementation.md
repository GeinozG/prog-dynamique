# Implémentation dans un jeu de Puissance 4

Maintenant que le fonctionnement de l'algorithme est claire, la partie la plus intéressante est de l'implémenter concrètement dans un projet pour le tester. Un jeu de puissance 4 fera parfaitement l'affaire car c'est un jeu aux règles simples, qui exige une certaine réflexion pour gagner et qui est plaisant à jouer.

## Choix des technologies

Dans la plupart des états, le jeu offre sept coups potentiels à jouer. Il s'agit de placé un jeton dans l'une des sept colonnes de la grille de jeu. Ainsi, le nombre de noeuds à explorer pour presque chaque état est de sept. Dans un arbre de profondeur n, le nombre de noeuds à évaluer sans élagage est donc de 7xxn. Cela signifie qu'avec une profondeur de 5, le nombre d'états possible est de 7xx5 = 16'807, pour une profondeur de 8, 7xx8 = 5'764'801. Dans ces conditions, il semblait judicieux de programmer l'algorithme dans un langage compilé, reconnu pour sa rapidité d'exécution. Malgré le défi que cela représente, le projet sera donc programmé avec le langage C++. De plus, comme le langage ne supporte pas nativement la gestion des fenêtres, afin de proposer un rendu graphique du jeu, le programme intégrera la librairie SDL2 qui offre une interface relativement simple à ces fonctionnalités.

## Structure générale du programme

Le programme est composé de plusieurs classes qui le divisent en 3 grandes parties :

1) Gestion de la fenêtre du jeu et le rendu graphique
2) Gestion du plateau et des règles du jeu
3) L'algorithme minimax

Schématiquement, le programme ressemble au diagrame de classes suivant (chaque rectangle représente une classe) :

```{figure} images/class_diagram.png
---
---

Appartenance de chaque grande classe par rapport aux autres.
```

A noter que chaque classe représentée dans le diagrame n'est instanciée qu'une seule fois dans le programe. Par exemple, la classe Board appartenant aux classes Game et Minimax n'est qu'une seule et même instance partagée entre ces deux classes par références. De plus, la classe Game est celle qui possède en tant que membres toutes les autres et qui les instancie. Tel un chef d'orchestre, c'est cette classe qui s'occupe de faire tourner le jeu, de gérer le tour des joueurs et d'informer le joueur humain lorsque le jeu est terminé.

### Fenêtre du jeu

En ce qui concerne la fenêtre du jeu, 

### Plateau de jeu

### Algorithme Minimax
# Implémentation dans un jeu de Puissance 4

Maintenant que le fonctionnement de l'algorithme est claire, la partie la plus intéressante est de l'implémenter concrètement dans un projet pour le tester. Un jeu de puissance 4 fera parfaitement l'affaire car c'est un jeu aux règles simples, qui exige une certaine réflexion pour gagner et qui est plaisant à jouer.

## Choix des technologies

Dans la plupart des états, le jeu offre sept coups potentiels à jouer. Il s'agit de placer un jeton dans l'une des sept colonnes de la grille de jeu. Ainsi, le nombre de noeuds à explorer pour presque chaque état est de sept. Dans un arbre de profondeur `n`, le nombre de noeuds à évaluer sans élagage est donc de 7 à la puissance `n`. Cela signifie qu'avec une profondeur de 5, le nombre d'états possible est de :

```{math}
7^5=16'807
```
Et pour une profondeur de 8 :

```{math}
7^8 = 5'764'801
```

Dans ces conditions, il semblait judicieux de programmer l'algorithme dans un langage compilé, reconnu pour sa rapidité d'exécution. Malgré le défi que cela représente, le projet sera donc programmé avec le langage C++. De plus, comme le langage ne supporte pas nativement la gestion des fenêtres, afin de proposer un rendu graphique du jeu, le programme intégrera la librairie SDL2 qui offre une interface relativement simple à ces fonctionnalités.

## Structure générale du programme

Le programme est composé de plusieurs classes qui le divisent en 3 grandes parties :

1) Gestion de la fenêtre du jeu et du rendu graphique
2) Gestion de la grille et des règles du jeu
3) Implémentation de l'algorithme Minimax

Schématiquement, le programme ressemble au diagramme de classes de la {numref}`Figure %s <class_diagram>` (chaque rectangle représente une classe).

```{figure} images/class_diagram.png
---
name: class_diagram
---

Relation de chaque grande classe par rapport aux autres.
```

```{note}
Chaque classe représentée dans le diagramme n'est instanciée qu'une seule fois dans le programme. Par exemple, la classe Board appartenant aux classes Game et Minimax n'est qu'une seule et même instance partagée entre ces deux classes par références. De plus, la classe Game est celle qui possède en tant que membres toutes les autres et qui les instancie. Tel un chef d'orchestre, cette classe s'occupe de faire tourner le jeu, de gérer le tour des joueurs et d'informer l'utilisateur lorsque le jeu est terminé.
```

### Fenêtre du jeu

En ce qui concerne la partie du programme qui gère la fenêtre du jeu, ce sont les classes Window et GraphicsManager qui s'en occupent.

#### Classe Window

La classe Window représente une abstraction très élémentaire d'une fenêtre. Son seul but est d'ouvrir une nouvelle fenêtre et de l'actualiser afin qu'elle ne plante pas. Ainsi, lorsque la classe est instancié, elle fait les démarches nécessaires pour ouvrir une fenêtre de la taille désirée et ferme cette fenêtre au moment où l'instance est détruite. Enfin, il suffit de l'actualiser grâce à sa méthode update() :

```{figure} images/window_class.png
---
---

Représentation schématique de la classe Window.
```

#### Classe GraphcisManager

Quand à elle, la classe GraphicsManager sert concrètement à gérer tout ce qui est chargement des textures et affichage des textures sur la fenêtre. Logiquement, cette classe à besoin d'avoir une référence à une instance de Window afin d'y afficher ses textures :

```{figure} images/graphics_manager_class.png
---
---

Représentation schématique de la classe GraphicsManager.
```

### Grille du jeu

A propos de la partie du programme qui gère la grille du Puissance 4, c'est la classe Board qui s'en occupe. Cette classe est la représentation abstraite du jeu et de ses règles. Concrètement, elle stocke la grille du jeu en mémoire et expose des méthodes qui permettent de la modifier en respectant les règles du jeu. Des méthodes permettent également d'obtenir des informations sur la grille du jeu (l'algorithme a besoin de savoir si un joueur a gagné ou si une case de la grille est vide par exemple) :

```{figure} images/board_class.png
---
---

Représentation schématique de la classe Board.
```

Comme la classe Board est capable de dessiner sa grille de jeu elle-même, elle possède une référence à la classe GraphicsManager qui expose des méthodes pour charger des textures et dessiner sur la fenêtre de la classe Window.

### Algorithme Minimax

Pour finir, c'est évidemment la classe Minimax qui s'occupe de la dernière partie du programme. Elle implémente l'algorithme Minimax, une fonction d'évaluation adaptée au Puissance 4 et optimise sa recherche avec l'élagage alpha-bêta. En outre, la classe possède une référence à la classe Board afin d'obtenir toutes les informations de la grille du jeu nécessaires à l'algorithme et modifier la grille pour jouer un coup :

```{figure} images/minimax_class.png
---
---

Représentation schématique de la classe Minimax.
```
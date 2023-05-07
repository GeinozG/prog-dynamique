# Algorithme Minimax

Tout d'abord, il s'agit de définir le fonctionnement de l'algorithme Minimax et son champ d'application. Ensuite, une présentation du procédé d'élagage alpha-bêta permettra d'introduire une optimisation simple mais très efficace de l'algorithme.

## Fonctionnement

### Arbres des possibilités

L'algorithme Minimax fonctionne en recherchant dans une situation donnée, parmi tous les coups possibles, lequel est le plus favorable pour le joueur et le plus défavorable pour son adversaire. Concrètement, il s'agit d'explorer de haut en bas un arbre des possibilités qui recense tous les coups possibles, sur plusieurs coups à l'avance (le nombre de coups à l'avance représente la profondeur de recherche de l'algorithme) :

```{figure} images/minimax_tree.png
---
---

Arbre des possibilités d'un jeu binaire, chaque noeuds représente un état possible du jeu.
```

Les noeuds bleus représentent les états du jeu lorsque c'est au joueur de jouer le prochain coup tandi que les noeuds rouges représentent les états lorsque c'est à l'adversaire de jouer.

### Evaluation des feuilles

Lors de son exploration de l'arbre, si l'algorithme atteint une feuille (un noeud de l'arbre qui ne se prolonge pas plus bas), soit parce que le jeu est arrivée à un terme, soit parce que la profondeur de recherche ne va pas plus bas par rapport au noeud initial, alors une fonction d'évaluation donne un score à l'état du jeu atteint :

```{figure} images/minimax_tree_score.png
---
---

Attribution d'un score à toutes les feuilles de l'arbre.
```

Plus le score est élevé, plus la fonction d'évaluation estime que le joueur est dans une position favorable. Tandis que plus le score est bas, plus l'adversaire est dans une position favorable.

### Fonction d'évaluation

Comme dit précédemment, la fonction d'évaluation permet à l'algorithme d'attribuer un score à un état du jeu en retournant une valeur qui représente l'avantage positionnel du joueur dans un état du jeu donné. Par exemple, si dans l'état du jeu étudié, le joueur a gagné le jeu, le score attribué à cet état sera significativement plus grand que dans un état où personne n'a encore gagné ou si c'est l'adversaire qui a gagné :

```{figure} images/evaluation_function.png
---
---

Entré/Sortie de la fonction d'évaluation.
```

### Déterminer le meilleur coup à jouer

Maintenant que chaque feuille de l'arbre à un score, il faut déterminer quel est le meilleur coup à jouer afin de poursuivre le chemin de l'arbre qui mène à l'état le plus favorable.

### Pourquoi n'évaluer que les feuilles /// commenté

## Champ d'application

## Elagage alpha-bêta
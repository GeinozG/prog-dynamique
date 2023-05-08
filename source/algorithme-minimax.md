# Algorithme Minimax

Tout d'abord, il s'agit de définir le fonctionnement de l'algorithme Minimax et son champ d'application. Ensuite, une présentation du procédé d'élagage alpha-bêta permettra d'introduire une optimisation simple mais très efficace de l'algorithme.

## Fonctionnement

### Arbre des possibilités

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

Le calcul se fait en prenant en compte le bénéfice de chaque joueur. Pour que cette évaluation puisse se faire il est important que le jeu qui implémente l'algorithme soit un jeu dit "à somme nulle". C'est-à-dire qu'il faut que le bénéfice d'un joueur entraîne un désavantage équivalent pour l'autre ; la somme des bénéfices et des désavantages doit donc être nulle. Ainsi, plus le joueur a de bénéfices par rapport à ses désavantages (qui correspondent aux bénéfices de l'adversaire), plus son score calculé est élevé.

### Déterminer le meilleur coup à jouer

Maintenant que chaque feuille de l'arbre à un score attribué, il faut déterminer quel est le meilleur coup à jouer afin de poursuivre le chemin de l'arbre qui mène à l'état le plus favorable. Pour ce faire, l'algorithme procède selon deux suppositions :

- Le joueur veut jouer les meilleurs coups
- L'adversaire va jouer tous les meilleurs coups pour lui.

C'est là que le nom de l'algorithme Minimax prend tout son sens. En effet pour chaque noeud non-feuille, l'algorithme lui attribue le score minimal ou maximal parmi tous les noeuds enfants (note de bas de page!). Les règles pour décider quel score attribuer à chaque noeud est intuitif et découle directement des deux suppositions énoncées précédemment :

- Si le noeud à l'étude est un état du jeu dans lequel le joueur joue le prochain coup, alors le noeud obtient le score maximum parmi ses noeuds enfants.
- Si c'est au tour de l'adversaire de jouer, alors le noeuds obtient le score minimal parmi ses noeuds enfants.

En procédant ainsi, chaque état du jeu est évalué en fonction du meilleur coup possible pour chaque joueur. C'est-à-dire que le joueur jouera les coups qui maximisent le score de chaque état du jeu, alors que l'adversaire jouera les coups qui minimisent ce score (d'où le nom Minimax) :

```{figure} images/minimax_value.png
---
---

Attribution des scores à chaque noeud non-feuille.
```

Maintenant que chaque noeud à un score, le joueur n'a plus qu'à jouer le coup qui maximisera son score. En l'occurence, dans l'exemple de l'image ci-dessus, le joueur à intérêt à jouer la coup qui l'amène au noeud de enfant de gauche (score=4) car c'est celui qui à le score le plus élevé parmi tous ses enfants.

Il est important de préciser qu'une évaluation statique des enfants directs du noeud racine (note de bas de page !!!) aurait pu générer un score beaucoup plus élevé au noeud de droite (score=-5)  et inférieur au noeud de gauche (score=4) car la fonction d'évaluation ne prend pas en compte les coups qui suivent. Ainsi, le joueur aurait pu prendre une décision qui se serait révélée défavorable quelques coups plus tard. C'est donc tout le principe de l'algorithme que d'éviter ce scénario.

## Champ d'application

A présent que le fonctionnement de l'algorithme ait été expliqué, il convient de préciser son champ d'application.

## Elagage alpha-bêta
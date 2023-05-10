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

A présent que le fonctionnement de l'algorithme a été expliqué, il convient de préciser son champ d'application. Comme mentionné précédemment, l'algorithme à besoin ne peut être employé que pour des jeux à somme nulle. Chaque le moindre avantage d'un joueur doit représenter un désavantage équivalent pour l'adversaire. De plus, en l'état, l'algorithme n'est adapté qu'à des jeux opposant deux joueurs. Il est facile de trouver des gens qui remplissent ces deux critères :

- Echecs
- Puissance 4
- Morpion
- Jeu du moulin
- Jeu de Go
- Jeu de dames

Cependant, l'application de Minimax ne se limite pas aux jeux, tout autre problème d'optimisation remplissant les deux critères sont des candidats potentiels à l'implémentation de l'algorithme.

## Elagage alpha-bêta

L'élage alpha-bêta est une optimisation très efficace de l'algorithme qui permet souvent de multiplier sa vitesse d'exécution par deux, dix ou même cent parfois. Le principe est simple à comprendre, comme son nom le suggère, il implique d'élaguer l'arbre des possibilités en n'évaluant pas tous les noeuds de l'arbre. Autrement dit, cela permet à l'algorithme d'éviter d'évaluer les noeuds qui ne contribuent pas à trouver le meilleur coup à jouer.

### Exemple

Comme un exemple vaut souvent plus qu'une longue explication, reprenons en considération un nouvel arbre dont les feuilles ont déjà été évalué par la fonction d'évaluation :

```{figure} images/alpha_beta_1.png
---
---

Exemple d'un arbre dont les feuilles ont toutes été évaluées.
```

Dans cet exemple, une feuille a été évalué inutilement, il s'agit de la dernière feuille à droite. En effet, sachant que l'ordinateur joue les noeuds bleus et l'adversaire les rouges, chacun cherche respectivement à maximiser ou minimiser le score. Ainsi, au moment d'évaluer la dernière feuille, il est possible de déduire que son noeud parent aura une valeur inférieure ou égale à son noeud frère (dont la valeur vaut -9). Mais comme le seul frère de son noeud parent vaut également -9, il est possible de déduire que le noeud racine privilégiera de toute façon la valeur -9 à une valeur potentiellement inférieure à -9. Ces deux déductions mènent à considérer l'évaluation de la dernière feuille comme superflue :

```{figure} images/alpha_beta_2.png
---
---

L'évaluation de la dernière feuille est superflue.
```

Ainsi l'évaluation finale de l'arbre ressemblerai à l'image suivante :

```{figure} images/alpha_beta_3.png
---
---

Elagage de la dernière feuille.
```

Il est important de se rendre compte que dans cet exemple, l'élagage peut sembler insgnifiant mais que dans des arbres plus grands et plus touffus, une énorme partie de l'arbre peut être élagué. En effet, une branche élaguée signifie que toutes les branches sous-jacentes le sont aussi. Ainsi, dans la plupart des cas, l'élagage diminue drastiquement le temps d'exécution de l'algorithme.

### Théorie

Pour comprendre quels sont les branches de l'arbre qui se font élaguer, il implique de comprendre en quoi consiste le nom "alpha-bêta" de l'élagage :

- Alpha représente la valeur maximal que le joueur actuel est garanti d'avoir à chaque étape de l'évaluation de l'arbre.
- Bêta représente exactement le contraire d'alpha, c'est-à-dire la valeur minimal que l'adversaire est garanti d'avoir à chaque étape.

Ces deux valeurs sont donc mise à jour après chaque évaluation selon ces critères, à chaque évaluation d'un état où le prochain coup revient à :

- Ordinateur : si la valeur évalué pour chaque enfant est *supérieur à alpha*, alors *alpha* prend cette valeur. Sinon, il est inutile de mettre à jour la valeur *d'alpha* car le *maximum* garanti au *joueur* est plus *élevé*.
- Adversaire : si la valeur évalué pour chaque enfant est *inférieur à bêta*, alors *bêta* prend cette valeur. Sinon, il est inutile de mettre à jour la valeur de *bêta* car le *minimum* garanti à *l'adversaire* est plus *petit*.

Il est important de se rappeler que l'ordinateur cherche toujours à maximiser le score de ses états contrairement à l'adversaire qui cherche à le minimiser.

Ainsi, un élagage a lieu de se produire lorsque, pour chaque noeud, bêta est inférieur ou égal à alpha. En effet, pour un noeud maximiseur, si bêta est inférieur ou égal à alpha, cela signifie que la valeur du noeud courant est au moins égal à alpha. Donc bêta (la meilleure valeur pour le noeud minimiseur parent) étant inférieur signifie qu'un meilleur coup était possible pour le noeud minimiseur parent. Evaluer les autres noeuds enfants devient donc inutile puisque le noeud minimiseur parent n'a pas intérêt à jouer le coup du noeud à l'étude (coupure alpha). Quant aux noeuds minimiseurs, si bêta est inférieur ou égal à alpha, cela signifie que la valeur du noeud courant est au plus égal à bêta. Donc bêta étant inférieur à alpha signifie que le noeud maximiseur parent a dans l'un de ses noeuds enfants explorés une valeur supérieur au noeud courant. Donc le joueur maximiseur ne va jamais prendre le chemin de l'arbre qui mène au noeud courant. Encore une fois, un élagage (coupure bêta) peut se faire dans ces conditions sans conséquence.
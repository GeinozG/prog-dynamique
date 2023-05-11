# Algorithme Minimax

Tout d'abord, il s'agit de définir le fonctionnement de l'algorithme Minimax et son champ d'application. Ensuite, une présentation du procédé d'élagage alpha-bêta permettra d'introduire une optimisation simple mais très efficace de l'algorithme.

## Fonctionnement

### Arbre des possibilités

L'algorithme Minimax fonctionne en recherchant dans une situation donnée, parmi tous les coups possibles, lequel est le plus optimal à jouer dans le but de gagner. Concrètement, il s'agit d'explorer de haut en bas un arbre des possibilités qui recense tous les coups possibles, sur plusieurs coups à l'avance (voir {numref}`minimax_tree`).

```{figure} images/minimax_tree.png
---
name: minimax_tree
---

Arbre des possibilités d'un jeu binaire, chaque noeuds représente un état possible du jeu.
```

Les noeuds bleus représentent les états du jeu lorsque c'est au premier joueur de jouer le prochain coup alors que les noeuds rouges représentent les états où c'est à son adversaire de jouer.

### Evaluation des feuilles

Lors de son exploration de l'arbre, si l'algorithme atteint un noeud feuille (un noeud de l'arbre qui n'a pas d'enfant), soit parce que le jeu est arrivé à un terme, soit parce que la profondeur de recherche ne va pas plus bas par rapport au noeud initial, alors une fonction d'évaluation donne une valeur au noeud feuille (voir {numref}`minimax_tree_score`).

```{figure} images/minimax_tree_score.png
---
name: minimax_tree_score
---

Attribution d'un score à toutes les feuilles de l'arbre.
```

Plus la valeur attribuée est élevée, plus la fonction d'évaluation a estimé que le premier joueur est dans une position favorable. Tandis que plus le score est bas, plus son adversaire est dans une position favorable.

### Fonction d'évaluation

Comme dit précédemment, la fonction d'évaluation permet à l'algorithme d'attribuer une sorte de score à un état du jeu en retournant une valeur qui représente l'avantage positionnel du premier joueur dans un état du jeu donné. Par exemple, si dans l'état du jeu évalué, le premier joueur a gagné, le score attribué à cet état sera significativement plus grand que dans un état où personne n'a encore gagné ou si c'est l'adversaire qui a gagné (voir {numref}`evaluation_function`).

```{figure} images/evaluation_function.png
---
name: evaluation_function
---

Entré/Sortie de la fonction d'évaluation.
```

Le calcul se fait en prenant en compte le bénéfice de chaque joueur. Pour que cette évaluation puisse se faire, il est important que le jeu qui implémente l'algorithme soit un jeu dit "à somme nulle". C'est-à-dire qu'il faut que le bénéfice d'un joueur entraîne un désavantage équivalent pour l'autre ; la somme des bénéfices et des désavantages doit donc être nulle. Ainsi, plus le joueur a de bénéfices par rapport à ses désavantages (qui correspondent aux bénéfices de son adversaire), plus la sa valeur positionnelle calculée est importante.

### Déterminer le meilleur coup à jouer

Maintenant que chaque feuille de l'arbre à une valeur attribuée, il faut déterminer quel est le meilleur coup à jouer afin de poursuivre le chemin de l'arbre qui mène à l'état le plus favorable. Pour ce faire, l'algorithme procède selon deux suppositions :

- Le premier joueur veut jouer les meilleurs coups. Il cherche donc à *maximiser* la valeur de chaque noeud, il s'agit du **joueur maximiseur**.
- Son adversaire ne va jouer que les meilleurs coups. Son objectif est donc de *minimiser* la valeur de chaque noeud, il s'agit du **joueur minimiseur**.

C'est là que le nom de l'algorithme Minimax prend tout son sens. En effet pour chaque noeud non-feuille, l'algorithme lui attribue la valeur minimale ou maximale parmi tous ses noeuds enfants. Les règles pour décider quelle valeur attribuer à chaque noeud est intuitif et découle directement des deux suppositions énoncées précédemment :

- Si le noeud à l'étude est un état dans lequel le joueur maximiseur joue le prochain coup, alors le noeud obtient la valeur maximale parmi ses noeuds enfants, il s'agit d'un **noeud maximiseur**.
- Si c'est au tour du joueur minimiseur de jouer, alors le noeud obtient la valeur minimale parmi ses noeuds enfants, il s'agit d'un **noeud minimiseur**.

En procédant ainsi, chaque état du jeu est évalué en fonction du meilleur coup possible pour chaque joueur (voir {numref}`minimax_value`).

```{figure} images/minimax_value.png
---
name: minimax_value
---

Attribution des valeurs à chaque noeud non-feuille.
```

Maintenant que chaque noeud à une valeur, le joueur maximiseur n'a plus qu'à jouer le coup qui maximisera la valeur de son futur état. En l'occurence, dans l'exemple de la {numref}`Figure %s <minimax_value>`, le joueur maximiseur a intérêt à jouer la coup qui l'amène au noeud enfant de gauche (score=4) car c'est celui qui a la valeur la plus élevée parmi tous ses enfants.

```{warning}
A ce stade, il peut être tentant de se demander pourquoi le programme n'effectue pas simplement une évaluation statique (purement positionnel par la fonction d'évaluation) des enfants directs du noeud racine. Ainsi, le joueur maximiseur n'aurait qu'à choisir le meilleur coup directement. C'est une fausse bonne idée. En effet, une fonction d'évaluation parfaite saurait attribuer une valeur exacte à un état quelconque du jeu, mais très souvent une telle fonction n'existe pas (encore). Dans ces conditions, une évaluation pourrait donner une valeur très généreuse à un état du jeu, mais quelques coups plus tard, il s'avèrerait que le coup jouer mène à une défaite par exemple. C'est pourquoi la recherche en profondeur de l'algorithme Minimax est indispensable dans ces conditions.
```

## Champ d'application

A présent que le fonctionnement de l'algorithme a été expliqué, il convient de préciser son champ d'application. Comme mentionné précédemment, l'algorithme ne peut être employé que pour des jeux à somme nulle. Le moindre avantage d'un joueur doit représenter un désavantage équivalent pour l'adversaire. De plus, l'algorithme n'est adapté qu'à des jeux opposant deux joueurs. Les jeux qui remplissent ces deux critères sont nombreux :

- Echecs
- Puissance 4
- Morpion
- Jeu du moulin
- Jeu de Go
- Jeu de dames

Cependant, l'application de Minimax ne se limite pas aux jeux, tout autre problème d'optimisation remplissant les deux critères énoncés sont des candidats potentiels à l'implémentation de l'algorithme.

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
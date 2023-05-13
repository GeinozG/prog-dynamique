# Détails de l'implémentation de la classe Minimax

Le chapitre précédent à présenté la structure globale du programme. Ce chapitre a pour objectif de reprendre le code présent dans la classe `Minimax` et de l'expliquer afin de réellement comprendre comment un tel algorithme peut être implémenter en C++ dans un Puissance 4.

## Minimax.h

Tout d'abord, c'est une bonne idée de prendre connaissance du code qui se trouve dans le fichier d'en-tête de la classe (Minimax.h). Il s'agit d'un fichier qui contient la déclaration de la classe et de tous ses membres : attributs et méthodes :

```{code-block} cpp
---
emphasize-lines: 26 - 34, 43, 51
---
class Minimax
{
public:
    Minimax(Board & board, SquareType humanType, SquareType computerType);
    ~Minimax();

    // Go through minimax algorithm and play on the board
    void play();

private:

    /*
    * Recursive function that go down the tree of possibilities
    * with alpha-bêta pruning optimisation. Each node get a value
    * based on the minimax principles.
    *
    * param position:   root state of the three
    * param bestMove:   get filled with the best move to play
    * param depth:      the depth of the recursive tree
    * param maxMoves:   maximum possible moves left to play from position
    * param alpha:      alpha for alpha-beta pruning
    * param beta:       beta for alpha-beta pruning
    * param player:     player that has to play the next move from position
    * Return: the value of the position passed in parameter
    */
    int minimax(
        BufBoard const& position,
        Vector2 & bestMove,
        int depth,
        int maxMoves,
        int alpha,
        int beta,
        SquareType player
    );

    /*
    * Evaluation function
    *
    * param position:   the position to be evaluated
    * param player:     the player that has to play the next move
    * Return: the value evaluated
    */
    int evaluatePosition(BufBoard const& position, SquareType player);

    /*
    * Get all possible moves to play from a position
    *
    * param position: the position to get moves from
    * Return: a vector (dynamic array) of the moves
    */
    std::vector<Vector2> getMoves(BufBoard const& position);

    // Game board
    Board & m_board;

    // Used in the evaluation function
    const int m_evaluationTable[6][7] = {
        { 3, 4, 5, 7, 5, 4, 3 }, 
        { 4, 6, 8, 10,8, 6, 4 },
        { 5, 8, 11,13,11,8, 5 }, 
        { 5, 8, 11,13,11,8, 5 },
        { 4, 6, 8, 10,8, 6, 4 },
        { 3, 4, 5, 7, 5, 4, 3 }
    };

    SquareType m_minimizerPlayer;
    SquareType m_maximizerPlayer;
};
```

Les lignes de code en évidence représentent les trois méthodes essentielles qui constituent l'algorithme :

1) La méthode `minimax()` est fondamentale, c'est une méthode récursive qui parcourt tous les états possibles du jeu (avec un élagage alpha-bêta) à partir de l'état courant du jeu. La méthode retourne à chaque fois la valeur d'une position et prend plusieurs paramètres :
    - `position` : Une position qui correspond à un état de la grille du jeu
    - `bestMove` : Une référence qui contiendra au final le meilleur coup à joué évalué
    - `depth` : La profondeur de recherche dans l'arbre des possibilités
    - `maxMoves` : Correspond au nombre maximum de coups théorique pouvant être joué avant de que la grille de jeu ne soit entièrement remplie
    - `alpha` : Variable contenant la valeur alpha de l'élagage alpha-bêta
    - `beta` : Variable contenant la valeur bêta de l'élagage alpha-bêta
    - `player` : Représente le joueur qui doit jouer le prochain coup
2) La méthode `evaluatePosition()` est, comme son nom l'indique, la fonction d'évaluation qui retourne une valeur par rapport à une position donnée. Elle est utilisée pour évaluer les noeuds feuilles et ne prend que deux paramètres :
    - `position` : L'état de la grille du jeu à évaluer
    - `player` : Représente le joueur qui doit jouer le prochain coup
3) La méthode `getMoves()` sert essentiellement à construire l'arbre des possibilités. Elle retourne, par rapport à une position donnée, tous les coups jouables possibles et ne prend donc qu'un paramètre :
    - `position` : Une position qui correspond à un état de la grille du jeu

## Implémentation des méthodes

Il s'agit à présent d'explorer l'implémentation de chaque méthode afin d'en comprendre le fonctionnement.

### getMoves()

La méthode `getMoves()` est simple à comprendre et à implémenter :

```{code-block} cpp
---
emphasize-lines: 9, 11, 12
linenos: true
---
std::vector<Vector2> Minimax::getMoves(BufBoard const& position)
{
    std::vector<Vector2> moves;

    for (int col = 0; col < BOARD_WIDTH; col++)
    {
        for (int line = BOARD_HEIGHT - 1; line >= 0; line--)
        {
            if (position.squares[line][col] == SquareType::Empty)
            {
                moves.push_back({ col, line });
                break;
            }
        }
    }

    return moves;
}
```

Les deux boucles `for` aux lignes 5 et 7 servent à parcourir toutes les cases de la grille de jeu, de bas en haut, de la gauche vers la droite (voir {numref}`getMoves_1`).

```{figure} images/getMoves_1.png
---
name: getMoves_1
---

Ordre dans lequel getMoves() parcours la grille de jeu.
```

Les lignes en évidences sont les plus intéressantes. A la ligne 9, le programme vérifie le type de la case présente à la ligne et à la colonne courantes. Si le type est égal à `SquareType::Empty` (si la case est vide), alors la ligne 11 est exécutée. Cette dernière ajoute dans la liste des coups possibles les coordonnées de la case vide. Enfin, la ligne 12 *casse* la boucle `for` qui parcourt la grille de bas en haut pour passer à la colonne suivante. En procédant ainsi, la méthode retourne exactement tous les coups possibles (voir {numref}`getMoves_2`).

```{figure} images/getMoves_2.png
---
name: getMoves_2
---

Tous les coups possibles.
```

### evaluatePosition()

Ensuite, la méthode `evaluatePosition()` est également simple à comprendre et à implémenter :

```{code-block} cpp
---
emphasize-lines: 9, 11, 13, 15, 20-22
linenos: true
---
int Minimax::evaluatePosition(BufBoard const& position, SquareType player)
{
    int value = 0;

    for (int line = 0; line < BOARD_HEIGHT; line++)
    {
        for (int col = 0; col < BOARD_WIDTH; col++)
        {
            if (position.squares[line][col] == m_maximizerPlayer)
            {
                value += m_evaluationTable[line][col];
            }
            else if (position.squares[line][col] == m_minimizerPlayer)
            {
                value -= m_evaluationTable[line][col];
            }
        }
    }

    SquareType winner = m_board.isWin(position);
    if (winner == m_maximizerPlayer) value += 100;
    else if (winner == m_minimizerPlayer) value -= 100;

    return value;
}
```

La variable `value` est celle qui représentera la valeur calculée finale. Elle est initialisée à la valeur `0` à la ligne 3 puis retournée à la ligne 24. Comme pour la fonction `getMoves()`, les boucles `for` aux lignes 5 et 7 parcourent la grille de `position` donnée en paramètre, cette fois, de gauche à droite, de haut en bas mais ça n'a aucune importance dans ce cas.

Concernant les lignes en évidences, les lignes 9 et 13 testent, pour chaque case de la grille, si le type correspond à une case occupée par l'un des joueurs, maximiseur ou minimiseur. Si c'est le cas, aux lignes 10 et 14, la valeur augmente ou diminue respectivement selon la valeur statique de la case occupée. En effet, l'attribut `m_evaluationTable` de la classe `Minimax` est un tableau à deux dimensions semblable à la grille du jeu. Cependant, chaque case à une valeur fixe en fonction de son importance dans le jeu. Concrètement, plus une case offre de possibilités d'aligner quatre jetons (c'est-à-dire gagner la partie), plus la case à une valeur statique importante. Ainsi, si l'un ou l'autre des joueurs à un jeton dans une case, la valeur de sa position augmente en fonction de la valeur statique de la case, causant un désavantage de valeur équivalente pour le joueur adverse (le Puissance 4 est un jeu à somme nulle). Dans les faits, la table d'évaluation est semblable à la {numref}`Figure %s <evaluationTable>`.

```{figure} images/evaluationTable.png
---
name: evaluationTable
---

Table d'évaluation statique du Puissance 4.
```

```{note}
Les cases au centre ont évidemment une valeur statique plus grande que les cases vers les bords car elles offrent un plus grand potentiel pour aligner quatre jetons.
```

Enfin, les lignes en évidences 20 à 22 parlent d'elle-même : La ligne 20 interroge la classe `Board` en lui demandant si un joueur a gagner. Les deux lignes suivantes testent le type du joueur qui a gagné. Si c'est le joueur maximiseur qui gagne dans cet état du jeu, alors la valeur retournée augmentera d'un coup de 100 car la victoire est le but recherché et il faut le faire comprendre à l'algorithme. A la ligne suivante, c'est tout le contraire. Si c'est le joueur minimiseur qui gagne, alors la valeur diminuera d'un coup de 100 car ça signifie la pire fin pour le joueur maximiseur, il faut également le faire comprendre à l'algorithme. Dans tous les autres cas (si aucun joueur n'a gagné), aucune alteration brusque de la valeur n'est nécessaire et la méthode retourne `value`.

### minimax()

Pour finir, il reste à comprendre l'implémentation de la méthode récursive `minimax()`, la plus intéressante :

```{code-block} cpp
---
linenos: true
---
int Minimax::minimax(
    BufBoard const& position,
    Vector2 & bestMove,
    int depth,
    int maxMoves,
    int alpha,
    int beta,
    SquareType player)
{
    assert(player != SquareType::Empty);

    SquareType winner = m_board.isWin(position);

    if (depth == SEARCH_DEPTH || maxMoves == 0 || winner != SquareType::Empty)
    {
        return evaluatePosition(position, player);
    }

    std::vector<Vector2> possibleMoves = getMoves(position);
    BufBoard childPosition = position;

    if (player == m_maximizerPlayer) // maximizer nodes
    {
        int maxValue = MINUS_INFINITY;

        for (Vector2 move : possibleMoves)
        {
            childPosition.squares[move.y][move.x] = player;

            int value = minimax(childPosition, bestMove, depth + 1, maxMoves - 1, alpha, beta, m_minimizerPlayer);
            if (depth == 0 && value > maxValue) bestMove = move;
            maxValue = std::max(value, maxValue);

            childPosition.squares[move.y][move.x] = SquareType::Empty;

            alpha = std::max(value, alpha);
            if (beta <= alpha) return maxValue;
        }

        return maxValue;
    }
    else if (player == m_minimizerPlayer) // minimizer nodes
    {
        int minValue = PLUS_INFINITY;

        for (Vector2 move : possibleMoves)
        {
            childPosition.squares[move.y][move.x] = player;

            int value = minimax(childPosition, bestMove, depth + 1, maxMoves - 1, alpha, beta, m_maximizerPlayer);
            minValue = std::min(value, minValue);

            childPosition.squares[move.y][move.x] = SquareType::Empty;

            beta = std::min(value, beta);
            if (beta <= alpha) return minValue;
        }

        return minValue;
    }
}
```

De la ligne 1 à 8, il s'agit de la signature de la méthode avec tous ses paramètres. Ensuite, à la ligne 14, la méthode teste si le noeud courant est un noeud feuille selon trois critères :

1) Si la profondeur courante est égale à la constante `SEARCH_DEPTH`, qui correspond à la profondeur de recherche maximale fixée.
2) Si le nombre de coups possibles restant à jouer est nul (la grille est pleine)
3) Si un joueur a gagné (`SquareType::Empty` est le type retourné par la méthode `isWin()` de la classe `Board` si aucun joueur n'a gagné)

Si le noeud courant est effectivement un noeud feuille, alors la ligne 16 retourne une évaluation statique de l'état du jeu grâce à la méthode `evaluatePosition()`.

Pour continuer, si le noeud courant est non-feuille, les lignes 19 et 20 préparent l'exploration récursive de l'arbre. A la ligne 19, la variable `possibleMoves` reçoit tous les coups à jouer possibles grâce à la méthode `getMoves()`. Quant à la ligne 20, la variable `childPosition` reçoit une copie de la position courante afin d'être modifiée par la suite.

La suite du code de la méthode peut globalement être décomposée en deux parties :

1) De la ligne 22 à 41, c'est la partie qui s'occupe des noeuds maximiseurs
2) De la ligne 42 à 60, la partie des noeuds minimiseurs

Pour la première partie, le code opère ainsi :

- Ligne 24 : Initialise la variable `maxValue`,qui représente la valeur finale du noeud, à la constante `MINUS_INFINITY` qui représente théoriquement la valeur la plus négative possible. Ainsi, la valeur par défaut de chaque noeud maximiseur ne sera jamais plus élevée que la valeur maximale calculée.
- Ligne 26 : La boucle `for` parcourt tous les coups possibles dans une variable `move` qui contient à chaque itération de boucle le coup à jouer.
- Ligne 28 : Le programme modifie la variable `childPosition` afin de simuler le coup du joueur passé en paramètre contenu dans la variable `move`. `childPosition` correspond donc maintenant à l'état d'un noeud enfant du noeud courant.
- Ligne 30 : La variable `value` correspond à la valeur du noeud enfant dont l'état est celui contenu dans la variable `childPosition`. C'est là que la récursivité à lieu. Pour affecter la valeur adéquate à `value`, il faut lui donner la valeur retournée par la méthode `minimax()`. Toutefois, il faut cette fois lui passer en paramètre `childPosition`, une profondeur incrémentée de 1 (`depth + 1`) et un nombre de coups possibles restants décrémenté de 1 (`maxMoves - 1`). Ainsi, la méthode se répète jusqu'à arriver à un noeud feuille. Dans ce cas, la ligne 16 est exécutée et la variable `value` du noeud parent du noeud feuille obtient la valeur statique de ce dernier (voir {numref}`recursive_value`).

```{figure} images/recursive_value.png
---
name: recursive_value
---

Evaluation récursive de la variable `value`.
```

- Ligne 31 : Le code parle de lui même mais pour résumer, la profondeur est nulle (noeud racine) et que la valeur calculé pour le noeud enfant courant est supérieure à la valeur maximale des noeuds enfants déjà évalués, alors le coup à jouer courant est le meilleur. Ainsi la variable `bestMove` prend la valeur de `move`.
- Ligne 32 : La valeur maximale `maxValue` prend la valeur maximale entre `value` qui vient d'être déterminée et `maxValue`qui est la valeur maximale jusqu'à présent.
- Ligne 34 : Remplace le coup simulé à la ligne 28 par une case vide.
- Ligne 36 : La variable `alpha` de l'élagage alpha-bêta qui prend comme valeur `value` si elle est plus grande qu'alpha.
- Ligne 37 : Comme expliqué dans le chapitre sur l'élagage alpha-bêta, si `beta` est inférieur ou égal à `alpha` alors une coupure à lieu et la valeur `maxValue` est retournée, empêchant ainsi l'exploration des autres noeuds enfants.
- Ligne 38-39 : Fin de l'itération de la boucle `for`, le noeud enfant suivant sera évalué jusqu'à qu'il n'y en ait plus. `maxValue` est finalement retournée.

La deuxième partie de la méthode est pratiquement la même sauf qu'elle cherchera à minimiser la valeur retournée et la valeur de `beta`.
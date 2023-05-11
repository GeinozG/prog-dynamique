# Détails de l'implémentation dans la classe Minimax

Le chapitre précédent à présenté la structure globale du programme. Ce chapitre a pour objectif de reprendre le code présent dans la classe Minimax et de l'expliquer afin de réellement comprendre comment un tel algorithme peut être implémenter en C++ dans un Puissance 4.

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

    SquareType m_humanType;
    SquareType m_computerType;
};
```

Les lignes de code en évidence représentent les trois méthodes essentielles qui constitue l'algorithme :

1) La méthode minimax() est fondamentale, c'est une méthode récursive qui va parcourir tous les états possibles du jeu (avec un élagage alpha-bêta) à partir de l'état courant du jeu. La méthode retourne à chaque fois la valeur d'une position et prend plusieurs paramètres :
    - position : Une position qui correspond à un état de la grille du jeu
    - bestMove : Une référence qui contiendra au final le meilleur coup à joué évalué
    - depth : La profondeur de recherche dans l'arbre des possibilités
    - maxMoves : Correspond au nombre maximum de coups théorique pouvant être joué avant de que la grille de jeu ne soit entièrement remplie
    - alpha : Variable contenant la valeur alpha de l'élagage alpha-bêta
    - beta : Variable contenant la valeur bêta de l'élagage alpha-bêta
    - player : Représente le joueur qui doit jouer le prochain coup
2) La méthode evaluatePosition() est, comme son nom l'indique, la fonction d'évaluation qui retourne une valeur par rapport à une position donnée. Elle est utilisée pour évaluer les noeuds feuilles et ne prend que deux paramètres :
    - position : l'état de la grille du jeu à évaluer
    - player : Représente le joueur qui doit jouer le prochain coup
3) La méthode getMoves() sert essentiellement à construire l'arbre des possibilités. Elle retourne, par rapport à une position donnée, tous les coups jouables possibles et ne prend donc qu'un paramètre :
    - position : Une position qui correspond à un état de la grille du jeu

## Implémentation des méthodes

Il s'agit à présent d'explorer l'implémentation de chaque méthode afin d'en comprendre le fonctionnement.

### getMoves()

La méthode getMoves() est simple à comprendre et à implémenter :

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

Les deux boucle for aux line 5 et 7 servent à parcourir toutes les cases de la grille de jeu de position, de bas en haut, de la gauche vers la droite (voir {numref}`getMoves_1`).

```{figure} images/getMoves_1.png
---
name: getMoves_1
---

Ordre dans lequel getMoves() parcours la grille de jeu.
```

Les lignes en évidences sont les plus intéressantes. A la ligne 9, le programme vérifie le type de la case présente à la ligne et à la colonne courantes. Si le type est égal à "Empty" (si la case est vide), alors la ligne 11 est exécutée. Cette dernière ajoute dans la liste des coups possibles les coordonnées de la case vide. Enfin, la ligne 12 *casse* la boucle for qui parcourt la grille de bas en haut pour passer à la colonne suivante. En procédant ainsi, la méthode retourne exactement tous les coups possibles (voir {numref}`getMoves_2`).

```{figure} images/getMoves_2.png
---
name: getMoves_2
---

Tous les coups possibles.
```

### evaluatePosition()

Ensuite, la méthode evaluatePosition(), également simple à comprendre et à implémenter :

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
            if (position.squares[line][col] == m_computerType)
            {
                value += m_evaluationTable[line][col];
            }
            else if (position.squares[line][col] == m_humanType)
            {
                value -= m_evaluationTable[line][col];
            }
        }
    }

    SquareType winner = m_board.isWin(position);
    if (winner == m_computerType) value += 100;
    else if (winner == m_humanType) value -= 100;

    return value;
}
```

La variable `value` est celle qui représentera la valeur calculée finale. Elle est initialisée à la valeur `0` à la ligne 3 puis retournée à la ligne 24. Comme pour la fonction `getMoves()`, les boucles `for` aux lignes 5 et 7 parcourent la grille de `position` donnée en paramètre, cette fois, de gauche à droite, de haut en bas mais ça n'a aucune importance dans ce cas.

Concernant les lignes en évidences, les lignes 9 et 13 testent, pour chaque case de la grille, si le type correspond à une case occupée par "l'ordinateur" ou par "le joueur humain". Si c'est le cas, aux lignes 10 et 14, la valeur augmente ou diminue respectivement selon la valeur statique de la case occupée. En effet, l'attribut `m_evaluationTable` de la classe Minimax est un tableau à deux dimensions semblable à la grille du jeu. Cependant, chaque case à une valeur fixe en fonction dans le jeu. Concrètement, plus une case offre de possibilités d'aligner quatre jetons (c'est-à-dire gagné la partie), plus la case à une valeur statique importante. Ainsi, si l'un ou l'autre joueur à un jeton dans une case, la valeur de sa position augmente en fonction de la valeur statique de la case, causant un désavantage de valeur équivalente pour le joueur adverse (le Puissance 4 est un jeu à somme nulle). Concrètement, la table d'évaluation est semblable à la {numref}`Figure %s <evaluationTable>`.

```{figure} images/evaluationTable.png
---
name: evaluationTable
---

Table d'évaluation statique du Puissance 4.
```

Les cases au centre ont évidemment une valeur statique plus grande que les cases vers les bords car elles offrent un plus grand potentiel pour aligner quatre jetons.

Enfin, les lignes 20 à 22 en évidences parlent d'elle-même : La ligne 20 interroge la classe Board en lui demandant si un joueur à gagner. Les deux lignes suivantes testent le type du joueur qui a gagné. Si c'est l'ordinateur qui gagne dans cet état du jeu, alors la valeur retournée augmentera d'un coup de 100 car la victoire est le but recherché et il faut le faire comprendre à l'algorithme. A la ligne suivante, c'est tout le contraire. Si c'est le joueur humain qui gagne, alors la valeur diminuera d'un coup de 100 car ça signifie la pire fin pour l'algorithme, il faut également le lui faire comprendre. Dans tous les autres cas (si aucun joueur n'a gagné), aucune alteration brusque du score n'est nécessaire et la méthode retourne la valeur.

### minimax()

Pour finir, il reste à comprendre l'implémentation de la méthode récursive minimax(), la plus intéressante :

```{code-block} cpp
---
emphasize-lines: 14-17, 19, 26
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

    if (depth == 0 || maxMoves == 0 || winner != SquareType::Empty)
    {
        return evaluatePosition(position, player);
    }

    std::vector<Vector2> possibleMoves = getMoves(position);
    BufBoard childPosition = position;

    if (player == m_computerType)
    {
        int maxWeight = MINUS_INFINITY;

        for (Vector2 move : possibleMoves)
        {
            childPosition.squares[move.y][move.x] = player;

            int weight = minimax(childPosition, bestMove, depth - 1, maxMoves - 1, alpha, beta, m_humanType);
            if (depth == SEARCH_DEPTH && weight > maxWeight) bestMove = move;
            maxWeight = std::max(weight, maxWeight);

            childPosition.squares[move.y][move.x] = SquareType::Empty;

            alpha = std::max(weight, alpha);
            if (beta <= alpha) return maxWeight;
        }

        return maxWeight;
    }
    else if (player == m_humanType)
    {
        int minWeight = PLUS_INFINITY;

        for (Vector2 move : possibleMoves)
        {
            childPosition.squares[move.y][move.x] = player;

            int weight = minimax(childPosition, bestMove, depth - 1, maxMoves - 1, alpha, beta, m_computerType);
            minWeight = std::min(weight, minWeight);

            childPosition.squares[move.y][move.x] = SquareType::Empty;

            beta = std::min(weight, beta);
            if (beta <= alpha) return minWeight;
        }

        return minWeight;
    }
}
```

De la ligne 1 à 8, il s'agit de la signature de la méthode avec tous ses paramètres.
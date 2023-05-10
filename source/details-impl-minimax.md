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

### minimax()
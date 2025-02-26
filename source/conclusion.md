# Conclusion

Pour conclure, bien que l'algorithme Minimax semble complexe à comprendre et à implémenter au premier abord, il n'en est rien si le principe de joueur maximiseur et adversaire minimiseur est bien compris. De plus, l'élagage alpha-bêta, un peu plus complexe à bien comprendre mais très facile à implémenter, permet de grandement diminuer le temps d'exécution de l'algorithme. Au final, avec une bonne fonction d'évaluation, les coups joués par l'algorithme sont surprenamment bons et le temps d'exécution est plus que convenable même avec des profondeurs relativement importantes. Cependant, le code n'étant pas parfait, il peut être amélioré et d'autres optimisations de l'algorithme peuvent être ajoutées pour un temps d'exécution encore plus faible.

```{note}
L'algorithme et le jeu ont été programmés en C++, un langage entièrement compilé. Probablement qu'en Python le temps d'attente entre chaque coup de l'algorithme aurait été plus long pour une même profondeur.
```
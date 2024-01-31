# LE LAPIN ET LES CARROTES

## Description
**FallDiagne** surnommé le lapin adorable aime trop les carrotes.
Mais malheuresement il est trés limité dans ses déplacements. il ne peut aller que **_vers le bas ou vers la droite_**. En supposant qu'il se trouve dans un espace ouvert qu'on peut modéliser comme un tableau de 2 dimensions (matrice).


Sur chaque cellule du tableau il y a soite la présence d'une carrote ou non. L'idée est d'aider notre mignon lapin a manger le maximum de carrotes possible entre un point S donné son point de depart et un point E le point d'arrivé. Tout en respectant les contraintes de déplacement de **FallDiagne**.

![Image Lapin Carrotes](images/img_lapin_carrote.png)

> [!NOTE]
> La [parenté à plaisanteries](https://www.cairn.info/revue-raisons-politiques-2004-1-page-157.htm) est une relation entre deux personnes dans laquelle l’une est autorisée par la coutume, et dans certains cas, obligée, de taquiner l’autre ou de s’en moquer; l’autre, de son côté, ne doit pas en prendre ombrage. Ce fut le cas entre les noms de famille **Diagne, Fall, Mbengue, Dieng**,... et le mien **NIANG**.

## Execution du programme

```
git clone https://github.com/bylaye/getMaxReward
```
```
cd getMaxReward
```

1. Mode non Graphique : CLI Mode
```
python
```
ou 
```
python3
```
```
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from MaxRewards import MaxRewards
>>> import initialise as m
>>> M = MaxRewards(m.MATRIX, m.START, m.END)
>>> M.get_
M.get_itineraries()  M.get_max_rewards()  M.get_movements()    
>>> M.get_max_rewards()
5
>>> M.get_itineraries()
[(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4), (4, 5)]
>>> M.get_movements()
's-d-b-d-b-b-d-d-b-d'
>>> 
```

2. Mode Interface Graphique
```
python GraficInterface.py
```
ou
```
python3 GraficInterface.py
```

> ![](images/simulation.png)

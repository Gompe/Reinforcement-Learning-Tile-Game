# Reinforcement-Learning-Tile-Game
Implementation of a tabular Reinforcement Learning Agent for a Tile Game

## The Game

We have a 3x3 grid and 8 1x1 pieces numbered from 1 to 8 distributed in the grid. The goal is to move the 1x1 pieces in such a way that the final configuration is the following:

```
| |1|2|
|3|4|5|
|6|7|8|
```

The only allowed move is to move a 1x1 piece to an adjacent empty square. For example:

```
|4|1|2|    |4|1|2|
|3|8| | => |3| |8|
|6|7|5|    |6|7|5|
```

The Reinforcement Learning agent learns how to solve this in the most efficient way and additionally learns when it is impossible to complete this task (Exactly half of the initial configurations lead to impossible games, due to the parity of the corresponding permutation).

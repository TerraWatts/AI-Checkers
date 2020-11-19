Practice Project: Checkers AI Using the Minimax Algorithm
Watts Dietrich
Nov 16 2020

In this practice project, the minimax algorithm is used to build an AI for the game of checkers.

The minimax algorithm works, in this case, by building a tree of possible moves, calculating a score for each branch,
and then executing the move which guides the game along the branch that has either the minimum or maximum score,
depending on which color the AI is controlling.

The AI seems to play fairly well. Its strength could be improved further by increasing the depth of its decision tree.
It currently uses a depth of 3, i.e. calculates outcomes 3 moves ahead. I use a depth of 3 because increasing the depth
beyond this starts to cause noticeable lag in the AI's decision time. This could be improved by further optimization
of the algorithm, which I may try to implement in the future.

There are also a few edge cases involving triple jumps with a king piece where the movement control system fails to
allow what should be legal by the rules of checkers. I'll have to re-work the movement system to fix this. For now, I
think it works well enough.

The Tech With Tim channel on youtube was an invaluable resource in figuring this out, see the link:
https://www.youtube.com/watch?v=RjdrFHEgV2o
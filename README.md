# snake-algorithm-challenge
Snake algorithm challenge solution by Francisco Arenas

## Solution
To solve the challenge I used a backtracking approach with functional programming. I didn't use an OOP solution because the input was strictly restricted and functional programming was a good approach for the algorithm. Even though, I think making classes for the data structures (instead of TypeAlias) would be a more maintainable solution.

## Improvements
If the efficiency of the algorithm were a must, the calculations of the body displacement could be done one time (instead of four, one per direction) at the beginning of the match statement  and then perform four times only the head displacement. I though this improvement would decrease the readability of the code (mainly because of working with pointers and copies) and for that reason is not implemented.

## Requirements
Python 3.10.2
Pytest==7.1.0. I used pytest instead of unittest because it is less verbose, more readable and faster

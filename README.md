# Oxbury Pathfind

Imagine representing a grid-shaped game map as a 2-dimensional array. Each value of this array is
boolean `true` or `false` representing whether that part of the map is passable (a floor) or blocked
(a wall).

Write a function that takes such a 2-dimensional array `A` and 2 vectors `P` and `Q`, with `0,0` being the top left corner of the map and returns the distance of the shortest path between those points, respecting the walls in the map.

eg. Given the map (where `.` is passable - `true`, and `#` is blocked - `false`)

```
. P . . .
. # # # .
. . . . .
. . Q . .
. . . . .
```

then `pathfind(A, P, Q)` should return `6`.

## What to do

1. Clone/Fork this repo or create your own
2. Implement the function described above
3. Provide unit tests for your submission
4. Fill in the section(s) below

## Comments Section

<!---
Please fill in the sections below after you complete the challenge.
--->

### What I'm Pleased With

I implemented the shortest path algorithm as a breadth-first search directly on the 2D array. 
Had the steps between coordinates been weighted, I would have used Dijkstra's shortest path algorithm. 

The pathfinder module handles input error cases, namely:
1. P and/or Q are outside the bounds of the 2D grid. 
2. There is no possible path between P and Q. 

I have achieved 100% code coverage (by line) of pathfind.py in the test_pathfind.py suite. This suite tests 
success cases, the error cases handled above, edge cases such as P and Q coinciding, and tests that the 
algorithm returns quickly on a 100x100 array.  


### What I Would Have Done With More Time

I would have added more accessors to the pathfind module to return properties of the map and a visual representations. 
I could also have enhanced the module to run as a script and accept input from the command line. 

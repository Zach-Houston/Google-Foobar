# Level 3

## precise_bomb.py

This program is pretty rough and could obviously be further optimized (especially just by simplifying some redundant if statements for clarity), but it was good enough for Google.
This program was meant for the following situation:
You start with 2 types of bombs.  You start with one of each.  Each generation, you can add one type's total to another type.  Example:

Trying to get the bombs to equal 7 4:

- Generation 1: 1 1
- Generation 2: 2 1
- Generation 3: 3 1
- Generation 4: 3 4
- Generation 5: 7 4

Therefore, the program will return 4 because it takes 4 generations to do it.  

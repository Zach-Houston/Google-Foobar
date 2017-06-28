
# Level 2

## tree.py

This program was made to traverse a perfect binary tree to find the parent node for each node given to it, indicated by its number.
The program mathematically computes it instead of creating an actual tree structure.

## largest_product.py

This program is fairly self explanatory, it creates the largest product in a given list of numbers.
This includes negative numbers as well.

## precise_bomb.py

This program is pretty rough and could obviously be further optimized, but it was good enough for Google.
This program was meant for the following situation:
You start with 2 types of bombs.  You start with one of each.  Each generation, you can add one type's total to another type.  Example:

Trying to get the bombs to equal 7 4:

- Generation 1: 1 1
- Generation 2: 2 1
- Generation 3: 3 1
- Generation 4: 3 4
- Generation 5: 7 4

Therefore, the program will return 5 because it takes 5 generations to do it.  

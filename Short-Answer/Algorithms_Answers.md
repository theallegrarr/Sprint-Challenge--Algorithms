#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because the code has a single loop which will only iterate n number of times


b) O(n^2) because the loop in the code has another loop nested inside it


c) O(n) even if there is no loop in this code, the recursive calls to bunnyEars will cause the code to be repeated n number of times based on how many bunnies are being counted


## Exercise II
This can be found with the binary search algorithm
1, First take the mid floor and throw an egg from it
2, if it breaks eliminate the current to top floors
3, then next take the mid floor between current_floor - 1 and the bottom
4, If it does not break at the middle then eliminate top to current_floor + 1
5, repeat till you find the lowest floor where the egg does not break

The complexity for the solution (Binary Search) would be O(log n)

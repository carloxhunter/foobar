# Task 3
## Subtask 2

Find the lowest number posible of steps to get from N number to 1.
You can only move by adding/substracting 1 or dividing the current number in 2.

Example: 
- solution(4) returns 2: 4 -> 2 -> 1
- solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Beware that the input is a string, where can have up to 309 characters therefore perfomance is important. I solved in 2 ways with while loop (passed all test) and recursive, this one give the result but with big numbers gets broken. But the logic is still right so i kept it in the repo.
# Merge Sort Vs Insertion Sort - Runtime-Comparison
Empirical analysis comparing the performance of Merge Sort and Insertion Sort across different input sizes to identify the crossover point where Merge Sort becomes faster.

Project Overview

This project measures and compares the execution time of two classic sorting algorithms: Insertion Sort and Merge Sort, using Python. The goal is to experimentally confirm their theoretical time complexities and determine at what input size (n) Merge Sort begins to outperform Insertion Sort.

Methods Summary:

Implemented Insertion Sort and Merge Sort in pure Python.
Used timeit.default_timer() to measure the runtime of each algorithm.
Tested across input sizes [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000].
Each test used randomly generated integer lists between 0 and 50,000.
Results were printed in a clean table for comparison and used to find the crossover point.

Key Findings:

Insertion Sort is faster for very small lists (n ≤ ~100).
Merge Sort becomes more efficient as list size increases because of its lower time complexity O(n log n) compared to O(n²).
The crossover point where Merge Sort starts winning was observed between n = 100 and n = 300, which matches theoretical expectations.

Technologies Used:

Language: Python 3.x
Modules: timeit, random
Platform: Any operating system (tested on Windows 11)

References:

GeeksforGeeks – Insertion Sort Algorithm - https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm

GeeksforGeeks – Merge Sort Algorithm - https://www.geeksforgeeks.org/dsa/merge-sort/

GeeksforGeeks – timeit Python examples -  https://www.geeksforgeeks.org/python/timeit-python-examples/

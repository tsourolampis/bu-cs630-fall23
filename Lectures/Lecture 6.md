Sep 21 2023

## Randomized Algorithms
- Difference between average case and randomized algs
	- In average-case analysis, we choose a random input
	- In a randomized algorithm, one makes a decision based on a random variable

### Bucket Sort
- Different elements placed in different buckets
- $T(n) = O(n) + \sum_{i=0}^{n-1} O(n_i^2)$
- What is the expectation of the $\sum_{i=0}^{n-1} O(n_i^2)$ term?
- Given $X = X_1 + ... + X_N$
	- $E[X] = E[\sum X_i] = \sum E[X_i]$
	- Linearity of expectation rule
- What about $Var(X) = \sum_{i=1}^{n} Var(X_i)$?
	- No because $Var(X) = E((X - \mu)^2)$
	- When expanded, there's a covariance term as well
	- If X is independent, Cov = 0

Given $X_i$ = # of elements in bucket i
- Given $X_i$ is uniformly distributed, every one of the n elements has an equal chance to go into any of the $k = n$ buckets
- $X_i = \sum_{j=1}^{n} Y_{ij}$
- $Y_{ij}$ = j-th element goes to the i-th bucket
- Z~Bernoulli(p) : Pr(Z = 1) = p, Pr(Z = 0) = 1 - p, $E[Z] = 1*p + 0*(1-p) = p$

- Expected value is $E[X_{ij}] = \frac{1}{n}$
- Number of inputs in bucket i: $n_i = \sum_{j=1}^{n} X_{ij}$
- Thus the expectation is $E[n_i] = \sum_{j=1}^{n} E[X_{ij}] = n \times \frac{1}{n} = 1$

## Randomized Algorithms
- So far, we have analyzed deterministic algorithms on random inputs, i.e., inputs that are “average”.
- **A Randomized algorithm** is an algorithm that makes random choices during its execution to influence its behavior
	- Instead of having a single, deterministic path of execution, a randomized algorithm can exhibit different behaviors on different runs, even when given the same input.

#### Types of Randomized Algorithms
- Monte Carlo
	- Bounded amount of time but have a probability of producing an incorrect answer.
	- Probability of error can often be made arbitrarily small by running the algorithm for a longer amount of time
- Las Vegas
	- Always produce the correct answer, but running time is a random variable.
	- Always terminates but time to do so isn't deterministic

#### Reminders: Mergesort
1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
3. Recurrence relation: T(n)=2T(n/2)+O(n), Time complexity: O(n log n)

### Reminder: Quicksort
1. Pick a pivot element from array.
2. Split array into 3 subarrays: those smaller than pivot, those larger than pivot, and the pivot itself.
3. Recursively sort the subarrays, and concatenate them.

### Some key differences
1. Merge sort: minimal work to split in half | Quick sort: Minimal work to merge the halves (they are sorted around the pivot)  
2. Merge sort worst case time complexity is O(n log n), Quicksort worst case time complexity is O(n2)  
3. What about space complexity?

### Quicksort
What if we used the median?
- Finding the median is a function that takes time

### Randomized Quicksort Analysis
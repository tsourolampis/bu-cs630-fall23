Sep 28 2023

## Median
- Sorting each group from low to high
- Given 5 or so groups, sorting the elements takes a constant time, approaches O(n)
- Choosing the median of each group and sort by increasing median
- The median of the medians is less than the medians that are greater than it and those elements that are greater than it and vice versa

- Goal: Not to get the exact median but to get a very good element to partition the array on

## Recursive Deterministic Alg: Select(A, k)
1. If |A| is constant size, sort it and return the k-th smallest element  
2. Partition A into subsets Ai of size 5.  
    Set:  
    X ← {Select(Ai,3)}   
    y ← Select(X, n/10)  
3. Z ← subset of elements in A less than y  
4. If |Z|>=k return Select(Z,k)  
    else return Select(A\Z, k-|Z|)

## Hats off - Linearity of Expectation
- n people take off their hats and shuffle it, the probability that a person gets their hat back is $\frac{1}{n}$
- Expected # of people who get their hats back?
- Linearity of Expectation: EV of the sum of random variables is equal to the sum of their individual expectations
	- Holds regardless of whether they are independent
- Let $X_1, ..., X_k$ be random variables
	- $\mathbb{E}[\sum_{i=1}^{k}c_i X_i] = \sum_{i=1}^{k}c_i \mathbb{E}[X_i]$
- Variance computation:
	- This problem is not pairwise independent
		- if n = 2, if the first person doesn't get their hat that means that the second person also won't get their hat back
	- Covariance

### Investment exercise:
- $\sigma_1 \text{ and } \sigma_2$ 
- $f = $
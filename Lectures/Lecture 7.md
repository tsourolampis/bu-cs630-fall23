Sep 26 2023
## Reminder: Randomized Quicksort
- Instead of searching for a median pivot, we select a random element as pivot
- Runtime is dominated by the number of comparisons
- **Observation: Let X be the number of comparisons over the entire execution of QS on n-element array. The run time is O(n+X).**
- Let T(n) be the expected number of comparisons that dominate the run time of QS.
	- Basis of recurrence: $T(0) = T(1) = 0$
	- Recurrence: $T(n) = n - 1 + \frac{1}{n} \sum_{\text{rank=1}}^n T(\text{rank}-1) + T(n - \text{rank})$
		- Explanation: For any element in an array, it has a particular rank from 1 to n, and that affects how the array is partitioned by elements larger or smaller than it
	- Due to symmetry (first term = last term, second term = second-last term, etc):
		- $T(n) = n - 1 + \frac{1}{n} \sum_{i=0}^{n-1}(T(i) + T(n-1)) = n - 1 + \frac{2}{n}\sum_{i=0}^{n-1}T(i)$
		- When the array is already sorted, it's a worst-case scenario
		- Substituting n-1:
			- $T(n-1) = n - 2 + \frac{2}{n-1}\sum_{i=0}^{n-2}T(i)$
			- $\Rightarrow \frac{T(n)}{n + 1} = \frac{T(n)}{n} + \frac{2(n-1)}{n(n+1)}$

## Median
- Using partition from quicksort
- The median is usually calculated in nlog(n) time (sort array, pick middle element)
- Using partition, you get the index of the pivot
	- if i + 1 = k, done!
	- if i >= k, then k-th smallest element is on the left
	- if i < k, then the k-th smallest element is on the "right"

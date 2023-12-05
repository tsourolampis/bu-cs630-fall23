Sep 7 2023
### Stable matching
- No entity from each group has an incentive to break their pairing for another

Algorithm
- Initially everyone is unmatched
- While some A a is unmatched:
	- Let b be a's most-preferred B to whom a has not proposed yet
	- if b is unmatched
		- b and a are paired (engaged)
	- else if b prefers a to current match a'
		- b breaks up with a' who becomes free again
		- b and are are engaged
	- else
		- b rejects a
- Return matched pairs

> Monotonic: a function that is either always increasing or decreasing

- Why does the algorithm always terminate?
	- Heuristically
		- Every B is always matched after their first pairing
		- Every A can only make n proposals, because they cannot propose to the same B twice
		- $P(O) = n^2$, $P(t+1) = P(t) - 1$
	- Observe that a proposal occurs during each iteration. Given that the max number of potential proposals is n^2 this substantiates the statement
		1. n^2 - n + 1 is actually attainable but not n^2 (why?)
		2. Design an instance where the G-S algorithm requires O(n^2) iterations

Analysis:
1. If m is free at some point in the execution, then there's a w to whom he hasn't proposed yet
	1. If all w are married, by proof of contradiction, n w married to n-1 m
	2. If not all w are married, then (not sure?)
2. Terminates with stable matching
	1. If m never proposed to w' (but if w' is higher on his priority list and w is the last match he made, this is a contradiction)
	2. If m proposed to w' but was rejected, that means w' had a better matching, but if the matching was unstable then that's not possible because m > m' for w'

All possible executions of the G-S algorithm produce the same output
- In other words, G-S returns {(m, best_valid_partner_of(m)) | m in M}
	- Proof by contradiction
	- Suppose arbitrary execution yields a stable matching M that violates this property {(m, best_valid_partner_of(m)) | m in M}
		- There exists a stable matching M' and an m such that m prefers w'=M'(m) to his partner w=M(m) in matching M
	- During the execution, w' must have rejected m.
	- Without loss of generality (this assumption is chosen arbitrarily, narrowing the proof to a particular case but not affecting the validity of the proof)
	- suppose this was the first occasion that during the execution a woman rejected a stable partner
	- Suppose the rejection happened due to the engagement of w' to m'
	- This means:
		- w' prefers m' to m
		- m' can have no stable partner that he prefers to w'
			- Because we assume this is the first occasion of rejected
	- Meaning that m' prefers w' to his partner in M'
		- Contradiction: m' is married to another w

Exercise: implement Gale-Shapley using dicts instead:

```python
men = {
	 'a': ['z', 'x', 'y'],
	 'b': ['y', 'x', 'z'],
	 'c': ['x', 'z', 'y']
}

women = {
	 'x': ['b', 'c', 'a'],
	 'y': ['c', 'a', 'b'],
	 'z': ['b', 'c', 'a']
}
```

### Average-case complexity
- Assumes some kind of randomness
- Analyzes runtime over all possible inputs

### Implementation Details:
- Implement using linked lists and arrays?
	- How do we represent our input in a programming language
		- Two 2D arrays for each group
	- Efficiently perform the following operations:
		- Identify a free m
			- Maintain the set of free m's as linked list, when we need to select a free m deletion takes O(1) and insertion takes O(1)
		- For an m we need to identify the highest rank w to who they have not proposed
			- Keep a pointer index for each m. Let the array next\[m\] contain the current proposal
		- For a w, we need to decide if w is engaged, and if yes, to who
			- Maintain an array
		- decide if a w will break up with her fiancee when they receive a proposal from another man
			- nxn table ranking
Oct 12 2023
## Hiring Problem
- If we want to hire the best candidate, we have to perform n interviews in the worst case
- Ordered according to a random permutation
- Take k elements to get a threshold in X = array of candidates
	- $M = \max_{1 \leq i \leq k}x[i]$
	- For $j \in k : n - 1$:
		- if x\[j\] > M
			- Hire J and stop
	- Hire n-th person
- Define $S_i =$ when candidate BEST is in position i
- Goal: $S = S_1 \cup S_2 \cup ... \cup S_i$
	- Pr(S) = sum of Pr(Si)'s from k+1 to n
- Case 1: worst case
	- If best candidate is in 1-k
		- You would traverse the entire array before realizing there's no one better
		- $Pr(S_i) = 0$ because you would never hire them since they're in the threshhold group
- Case 2: Person is in position i
	- $M_k = \max_{1 \leq i \leq k} x(i)$
	- All k + 1, k + 2... up to i-1 (where the best candidate is) have to be less than Mk
	- Pr( ) = k/i-1
		- The probability that the maximum of the i-1 numbers resides in the first k positions
	- Pr(Max in i) = 1/i-1
	- Pr(max among i-1 is located in k) = k*(1/i-1)
	- $Pr(S_i) = \frac{1}{n} * \frac{k}{i-1}, i \geq k+1$
	- The probability that the max candidate is at a position times the probability that the second-highest candidate is in k and that all the numbers after k are smaller than the second-highest candidate
	- $Pr(S) = \sum_{i=k+1}^n \frac{1}{n} * \frac{k}{i-1}, i \geq k+1$
	- $= \frac{k}{n}(\sum_{i=k+1}^n\frac{1}{i-1}) = \frac{k}{n}(\frac{1}{k} + \frac{1}{k+1} + ... + \frac{1}{n-1})$
	- $= \frac{k}{n}(1 + \frac{1}{2} + ... + \frac{1}{k-1} + (\frac{1}{k} + \frac{1}{k+1} + ... + \frac{1}{n-1}) - (1 + \frac{1}{2} + ... + \frac{1}{k-1}))$
	- $H_{n-1} = \frac{1}{k} + \frac{1}{k+1} + ... + \frac{1}{n-1}$
	- $H_k = 1 + \frac{1}{2} + ... + \frac{1}{k-1}$
	- $\approx \frac{k}{n}\log(\frac{n}{k})$
	- $k = \frac{n}{e}$
- If you choose a very large k or a very small k, you get closer to choosing a non-optimal candidate

## Ramsey Numbers
- Suppose you have 6 people, some of them know each other and some of them don't
- How many possible edges? $n*(n-1)$ or ${6 \choose 2}$
- Let $K_6 =$ clique of 6 nodes
- 2-coloring of $K_6$, a green edge means they know each other and a black edge means they don't
- How many triangles of people that know each other? Monochromatic triangle (either green or black)
- $\forall$ 2 colorings there exists a monochromatic triangle
	- In N = 5, possible (draw a star of green edges, no green triangles formed)
	- In N = 6, there will always exist at least 1 black or 1 green triangle
- Proof: Take one person A from A, B, C, D, E, F
- 5 people and 2 colors
	- By pigeonhole principle, one of the colors will appear at least three times (ceil(5/2))
	- Say it's Green, and say there's a green line to B,  C, D. There are lines BC, CD, and BD. If any of those are green, we found a green triangle. If not, BCD forms a black triangle
- R(m, n) = k
	- Given k nodes, no matter how the graph is colored, you will get a monochromatic clique of m nodes or a monochromatic clique of n nodes

- Theorem: if ${n \choose k}2^{1 - {k \choose 2}} < 1$ then R(k, k) > n
- Probabilistic Method Alon-Spencer
	- Proof:
		- Suppose we two-color $K_n$ randomly
		- It suffices to show a 2-coloring that doesn't yield a monochromatic k-clique
		- Given k choose 2 edges
			- P(edge being a certain color) = $\frac{1}{2^{k \choose 2}} = 2^{1 - {k \choose 2}}$
			- Consider any set of k nodes in S, |S| = k
			- Then, the probability that S is monochromatic is $2^{1 - {k \choose 2}}$
			- There are n choose k choice sets
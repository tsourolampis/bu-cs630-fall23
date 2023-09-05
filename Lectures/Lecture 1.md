Tue Sep 5 2023
- [Slides](https://docs.google.com/presentation/d/1-7Xe0VczOGcDYI_Q37U71xoADL6fneUIQez4WpioPl4/edit?pli=1#slide=id.g10fb791f0ed_0_0)
#### Some of the topics to be covered...
- Basic algorithmic techniques and data structures
- Linear algebraic algorithms
- The random projection method and its applications to algorithm design
- Streaming algorithms: input comes as a stream
	- Big data
- Graph algorithms
	- MSTs, matchings, shortest paths, diameter, flows, min cut, max cut, spectral graph theory
- Linear programming and duality
- NP-hardness reductions and other complexity classes
- Approximation algorithms
- Randomized algorithms
- Convex optimization
	- Gradient descent, backpropagation
- Miscellaneous algorithmic topics
	- Computational geometry, cryptography, perceptron algorithm, sub-modular optimization
#### Max Cut
- An NP Hard problem
- Partition a graph such that # of edges between two partitions is maximized
- $2^n - 1$ possibilities including the empty set
- Find the expected # of edges crossing given a random partition
### Math
$f(x) = x^2, x \in \mathbb{R}$
$f(\vec{x}) = <\vec{x}, \vec{x}>$
$x = (x_1, ..., x_n)$
$\therefore x^2_1, ... x^2_n$
$\frac{df}{d\vec{x}} = (2x_1, 2x_2, ..., 2x_n)$
$= \frac{2f}{2x}$
## Approximation Algorithm
- An optimal solution may be NP hard, which means it can take an exponential amount of time to solve the problem.
- Design an approximation algorithm such that
- $OPT > C_{output} > \alpha OPT$, where $\alpha = 0.5$
## Stable Matchings
- A 1-1 mapping of a set of n entities in two sets that contains no entities from either set who would agree to leave the current pairing for another pairing
- A matching/independent edge set in an undirected graph is a set of edges without common vertices
- A perfect matching is a matching that matches all vertices of the graph
	- Bipartite matchings
	- Perfect matching need not be unique
		- Suppose two sets with n nodes that is fully connected
			- \# of possible edges = $n^2$
			- \# of permutations of perfect matches = $n!$
	- How would you find a perfect matching? Max flow...
	- How would you count perfect matchings of a bipartite graph
		- \#P (sharp p) complete
		- Permanent of matrix (similar to determinant of matrix)
### Definition
- Given perfect matching M, an unmatched pair of a A (a) and a B (b) form an unstable pair if both:
	- a prefers b' to their match M(a)
	- b prefers a' to their match M(b)
- A stable matching is a perfect matching with no unstable pairs
- Given the input and a perfect matching M how to test if M is stable?

```
flag = true
For each A a:
	For each B b that ranks higher in a's preference to M(a):
		if b prefers a to their match M(b):
			flag = false
			return flag
return flag
```

Time complexity: $O(n^2)$
- Ranking table of N a's x N b's (adjacency matrix):
	- ranking\[b, a\] vs ranking\[b, M(b)]

### There is always a stable matching...
- If the graph is bipartite (if not, then stable roommate problem)

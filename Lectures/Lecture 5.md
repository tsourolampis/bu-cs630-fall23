Sep 19 2023
## Loop Invariants
Key to analyzing and implementing algorithms with repetition

### 1. Designing an iterative algorithm
- Input: Undirected graph G s.t. each node has at most d neighbors
- Output: Coloring of nodes with (at most) d+1 distinct colors so that no two adjacent nodes have the same color
- Goal: design an iterative algorithm

#### One method:
- A (partial) coloring of the nodes is proper if no two colored adjacent nodes have the same color
- Loop invariant: after coloring i nodes, we have a proper coloring
- Measure of progress: # of colored nodes. In each iteration we color at least one node
- How to maintain the loop invariant from i to i+1?
	- Ensure that the color chosen is a different color from any colors assigned to a neighbor
	- Given that a node has at most d nodes, if you try to use all the colors to color the node's d neighbors, there's at least 1 color left that you can use to color the node.
- Action: 
	- Consider any uncolored node v
	- It has at most d neighbors, some possibly already colored
	- By the pigeonhole principle, there's always one or more colors available since there's d + 1 colors available and the max # of neighbors is d
	- Color v with that color

### 2. Proving impossibility
- Mutilated chessboard problem: Place 2x1 dominoes on a grid with corners on one diagonal removed
- Initially, board is empty (32 black tiles, 30 white tiles if 2 white tiles are removed)
- Key insight: each domino covers one black and one white
- Loop invariant: Number of black and white tiles covered is equal
- Algorithmic step: place a domino
	- Loop invariant maintained as count of black and white tiles increases by 1 per domino place
- Once we place 30 tiles, we will have 2 black squares left, where a domino cannot be placed
- This is a contradiction

### 3. Analyzing Mystery sequences
- Start with (a, b) where 0 < b < a and generate a sequence of points $(x_n, y_n)$ according to the rules:
	- $x_0 = a$
	- $y_0 = b$
	- $x_{n+1} = \frac{x_n + y_n}{2}$ (arithmetic mean)
	- $y_{n+1} = \frac{2x_ny_n}{x_n + y_n}$ (harmonic mean)
- Loop invariants?
	- See that the product remains the same
	- $x_{n+1}*y_{n+1} = \frac{x_n + y_n}{2} * \frac{2x_ny_n}{x_n + y_n}$
	- $\lim_{n\rightarrow \inf} x_n = \lim_{n\rightarrow \inf} = y_n$
	- To solve for convergence: removing the recurrence/iteration in the equation and solving for the system
		- $x = \frac{x + y}{2}, y = \frac{2xy}{x + y}$
- Use loop invariant to show that the sequence converges to $(\sqrt{ab}, \sqrt{ab})$


### 4. The sorting problem:
- Input: A sequence of pointers containing numbers
- Output: A permutation/reordering
- Is the output the same for any reordering? Depending on the key upon which we are sorting

#### Selection Sort
- Loop invariant:
	- All the numbers on the left are less than the numbers on the right
	- To maintain this: find the smallest number on the right and move it to the rightmost position on the left

#### Insertion Sort
- Loop invariant: similar
#### Bucket Sort
- Sort items by bucket (range of certain values can enter a bucket)
- Buckets are sorted (using insertion sort on each bucket)
- If n elements go to bucket i, we know that insertion sort requires $O(n_i^2)$ time
- $Var(X) = E(X^2) - (E(X))^2$
- $E(X^k) =$ kth moment

Prove
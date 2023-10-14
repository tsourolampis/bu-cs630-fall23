Sep 12 2023

$$
\newcommand{\floor}[1]{\lfloor #1 \rfloor}
$$
## Priority Queues
- Airport check-in system
	- Imagine passengers are processed based on their flight departure times
		- A leaves in 3h
		- B leaves in 1h
		- C leaves in 2h
- Passengers have different priorities
	- Using a priority queue, the order in which passengers are processed will be: B, C, A
- Ensures that those in most urgent need (imminent departures) are addressed first, optimizing the airport's ability to get passengers to their gates on time

### Data Structure
- Set of elements S, each associated with a key
```
Passenger id: A
First name: Rithvik
Last name: Doshi
Pass id: 31234
key(A) = 2
```

Priority depends on condition:
- Min heap: lower key <-> higher priority
- Max heap: in python, same as a min heap but take the negative
#### Basic ADT
```
insert(object, priority)
extractTopPriority()
update(object, new_priority)
isEmpty()
```

Goal: Learning about Entropic Lower Bounds this week

### Naive implementations:
- Unsorted array:
	- Takes linear time
- Sorted array
	- Binary search but sorting takes time and array insertion
- Sorted linked list
	- Can't use binary search

### Binary heaps
- Place elements in a binary tree, node with highest priority sits at the root
	- The priority of every node is higher than (or equal to) that of its children
	- All levels are completely filled, except possibly the last one, which is partially filled form the left

#### Implement heap as an array:
```
leftChild[i] = 2i (if you're starting at 1, else 2i + 1)
rightChild[i] = 2i+1 (if you're starting at 1, else 2i + 2)
Parent[i] = floor(i/2) (if starting at 1, else floor((i-1)/2))
```

#### Max heap property: $A[Parent[i]] \geq A[i]$
#### Min heap property: $A[Parent[i]] \leq A[i]$

### ? What are the minimum and max numbers of elements in a heap of height h?

$$2^h - 1 + 1 = 2^h \leq n \leq 2^{h+1} - 1$$
- Given an n-element heap of height h, we can deduce that
$$h \leq \log_{2}n < h + 1 => h = \floor{\log_{2}n}$$

https://www.cs.usfca.edu/~galles/visualization/Heap.html

#### Time complexity: O(log(n))
- We can sort n elements by first inserting them into the heap and then removing them one by one
- **Claim**: any sequence of priority queue operations that results in the sorting of n numbers, must take time at least proportional to n log n in total
- Thus, efficient implementation would be O(log n) for insertion and extraction of minima

[Entropy and counting, pages 2-4](https://www.tcs.tifr.res.in/~jaikumar/Papers/EntropyAndCounting.pdf)
- Entropy always increases as we move into the future
- Uncertainty, measure of surprise
- Definition of entropy: random variable X with finite range:

$H[X] = - \sum_{x \in range(X)} Pr(X=x)\log_{2}Pr(X=x)$

Coin toss entropy
$H[p] = -p\log(p)-(1-p)\log(1-p)$ for $0<p<1$
$H[0] = H[1] = 0$

#### Shannon Entropy Fundamental Limits on Communication
- Value of the random variable X is presented to A who has to describe it to B
- A and B decide on encoding of the range of (X)
- H\[X\] is the average number of bits A needs to send to B to reveal the value of X under the best encoding

### Joint Entropy

$$H[X, Y] = - \sum_{x\in range(X), y \in range(Y)}Pr(X=x, Y=y)\log_{2}Pr(X=x, Y=y)$$
$$= - \sum_{x, y}p(x, y)\log_{2}p(x, y)$$
- Conditional entropy of X given Y: $H[X|Y] = \mathbb{E}[H[X_Y]]$
- where $X_Y$ is a random variable such that $Pr(X_Y = x) = Pr(X=x | Y=y)$
$$H[X,Y]=H[X] + H[Y|X]$$
$$H[X,Y|Z]=H[X|Z] + H[Y|X,Z]$$
#### Entropy subadditivity
Oct 5 2023

## Weak Law of Large Numbers - Confidence Intervals
- ![[Screenshot 2023-10-05 at 9.52.57 AM.png]]
- $\alpha$ is a means to quantify the probability that the empirical average falls within the given range

## Algorithm for Estimating $\pi$
- Using a monte carlo algorithm: darts
- Points that fall within a circle/points that fall within a square
- Estimate is $\frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi}{4}$
- **We know by the WLLN that our approximation of π should improve**
- ![[Screenshot 2023-10-05 at 9.58.23 AM.png]]
- The distribution of $S_n$ is Binomial (the sum of n bernoulli trials with probability p)
- **Using the WLLN that we obtained using Chebyshev’s inequality, we get that:**
- ![[Screenshot 2023-10-05 at 9.59.02 AM.png]]
- If $\epsilon , n$ are given we can compute the confidence $1 - \delta$

### Doulion Problem
- Randomized algorithm to count triangles
- Make a random subset of the edges, where probability an edge is selected is p
- $T = \sum_{i = 1}^{t} X_i$
- $X_i = 1 \text{ if the ith triangle survives, } 0 \text{ otherwise}$
- Probability that a triangle survives: $p^3$
- Expected # of triangles = $t*p^3$ where t is the true # of triangles in the subset
- $E_p$ = {sample of edges}
- Count T = # triangles in $E_p$
- Return $\frac{T}{p^3}$
- Triangles that share the same edge are not independent
- Covariance: 
	- $Cov(X, Y) = E(XY) - E(X)E(Y)$
	- $E(XY) = 0*Pr(XY = 0) + 1*Pr(XY = 1)$, $E(X)E(Y) = p^3*p^3 = p^6$
	- $= p^5 - p^6$ (given that if triangles share one edge the probability that all 5 edges survive is $p^5$)
## Coupon Collector Problem
- Consider randomly tossing identical balls into n bins, numbered 1...n, where the tosses are independent
- How many balls must one toss until every bin contains at least one ball?
- Let's define $X_t$ to be equal to the number of non-empty bins after throwing t balls
- ![[Screenshot 2023-10-05 at 10.23.58 AM.png]]
- ![[Screenshot 2023-10-05 at 10.24.14 AM.png]]
- ![[Screenshot 2023-10-05 at 10.24.46 AM.png]]
- Expectation of Geometric RV is $\frac{1}{p}$
- Say you have 4 buckets
	- To get a ball into first bucket, you only have to throw one ball
	- To get a ball into a second bucket, you have a chance of $\frac{3}{4}$
	- To get a ball into a third bucket, you have a chance of $\frac{2}{4}$
	- To get a ball into the last bucket, you have a chance of $\frac{1}{4}$
	- As such, your expected value of balls is 1 + $\frac{4}{3}$ + $\frac{4}{2}$ + $\frac{4}{1}$ = 8 $\frac{1}{3}$
- Related to Markov Chains

## Randomized Hire Assistant
- Randomly permute the list of candidates
- best = 0
- for i in i to n:
	- If candidate i is better than candidate best
		- Best = i
		- Hire candidate i
- Suppose for each hiring we pay c dollars. What is the expected hiring cost of the procedure?
Sep 14 2023

### Shannon entropy
- $H[X] = - \sum_{x \in range(X)} p_x log(p_x)$

#### Joint Entropy:
- Given discrete random variables $X, Y$, follow rules of joint probability distribution
	- If it's independent variables, it's the product of the probabilities since $Pr(X = x, Y = y) = Pr(X = x)\times Pr(Y=y)$
	- If it's dependent this is not the case
- Given $Z = (X, Y)$, $H(Z) = - \sum_{z \in range(Z)} p_z \log (p_z)$
- Range(z) = $X\times Y$ (something like $\{(0,1), (0,2), (10,1), (10,2)\}$)
- Probabilities: $Pr(0, 1) = \frac{1}{4}, Pr(0, 2) = \frac{1}{2}, Pr(10, 1) = 0, Pr(10, 2) = \frac{1}{4}$
- $\therefore H(Z) = - \frac{1}{4}log(\frac{1}{4}) - \frac{1}{2}log(\frac{1}{2}) - \frac{1}{4}log(\frac{1}{4})$
- Entropy is measured in bits

Conditional entropy: Expected value of the entropy (probability of outcome times entropy of outcome)

If probability of an outcome is dependent, its entropy is less likely to be high

Probability chain rule translates to Entropy subadditivity (product changes to addition through log rules)

#### Facts about entropy
- $H[X] \leq log_{2} |range(X)|$ With equality when X is uniform (all probabilities of possible outcomes are the same)
	- Proof: why is this the case (plug in probability and do the math)
- $H[X] \geq H[X|Y]$ (information never hurts)
- Let X be a random variable and let g(X) be some deterministic function of X
	- $H[X] \geq H[g[X]]$
	- Equality holds iff g is invertible (can go from range of functions back to domain, $x = g^{-1}(y)$
	- Joint entropy of the two random variables
	- If invertible, ordering the variables shouldn't matter

### Proving Lower Bound
- Choose X as a random permutation of \[n\] with uniform distribution.
	- Then $H[X] = log_{2}(n!)$
- Let $\{Y_1, ..., Y_t\}$ be the outcome of t comparisons when the actual ordering of the input is given by X. Thus $\{Y_1, ..., Y_t\}$ are random variables dependent on X
- Furthermore $X=f(Y_1, ..., Y_t)$ when t is large enough to be able to reconstruct X from the pairwise comparisons

Example: n = 3
$Y_1 = x_1 < x_2$
$Y_2 = x_1 < x_3$
1, 2, 3 Yes
1, 3, 2 Yes
2, 1, 3 No
2, 3, 1 No
3, 1, 2 No
3, 2, 1 No

### Priority queues
- Min or max heap where
	- Every parent's value is less/more than its children
	- Every subtree is also a min/max heap
- Heapify-up: inserting a leaf to the root of the tree and shifting it to make a valid tree
- Heapify-down:


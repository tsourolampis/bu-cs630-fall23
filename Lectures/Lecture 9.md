Oct 3 2023
## Bit of Calculus + Solving Recurrences
- Cutting a pizza so that each new cut creates the maximum # of pieces
- Solution is to draw a line s.t. all existing lines are intersected
- Upper bound: n new pieces created for every nth line
- Recurrence: $L_n = L_{n-1} + n$
- Solution for the recurrence:
	- Given derivative = $lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}$
	- $\frac{L_n - L_{n-1}}{n - (n-1)}$

- Another example: discs on some rows, moving stack from 1 row to another
- Solution: Break up problem for n discs:
	- T(n) = f(1...n, A to B via C) comprised of:
		- T(n-1) = f(1...n-1, A to C via B)
		- 1 = Move disk n from A to B
		- T(n-1) = f(1...n-1, C to B via A)
- Recurrence: T(n) = 2T(n-1) + 1
	- Given $f(n) = 2f(n-1) \rightarrow 2^{n-1}$
	- 1 + T(n) = 2T(n-1) + 1 + 1
	- 1 + T(n) = 2(T(n-1) + 1)
	- Change of variables: Q(n) = 1 + T(n)
	- Q(n) = 2Q(n-1)
	- $Q(n) = 2^{n-1}$
	- $T(n) = 2^{n-1} - 1$

## Randomized Algorithms
### Markov's Inequality
- Given that X is a non-negative random variable and suppose that E\[X\] exists (E\[X\] is finite and some number not infinity)
- $$\text{For any $t>0$, } Pr(X \geq t) \leq \frac{E[X]}{t}$$
- Proof:
- ![[Screenshot 2023-10-03 at 10.08.10 AM.png]]
- In other words, the expectation from 0 to t + t to infinity is greater than the expectation from t to infinity which is greater than t times the probability that X > t

- X~Bin(n, p): n = 1000, p = 0.1
- $Pr(x \geq 400) = {{1000}\choose{400}}*0.1^{400}*0.9^600 + ... = \sum_{k=400}^{n}{n\choose k}*p^k*(1-p)^{n-k} \leq \frac{1}{4}$
- This is not the tightest bounds since it only uses the expectation
- Used to prove other inequalities

$Pr(X \geq t)$ but t may be negative
- Square it maybe, absolute values

### Chebyshev's inequality
- Let $\mu = \mathbb{E}[X], \sigma^2 = \mathbb{Var}[X]$
- Then, $Pr(|X - \mu|) \geq t) \leq \frac{\sigma^2}{t^2}$
- X~Bin(n, p): n = 1000, p = 0.1
- Variance = $n*p*(1-p)$
- $Pr(X \geq 400) = Pr(X - 100 \geq 300) \leq Pr(|X - 100| \geq t) \leq \frac{\mathbb{Var}}{t^2} = \frac{90}{300^2} = 0.001$
-  Why? Binomial can be approximated by Gaussian
- Bin(n, p) ~ N(np, np(1-p))

- Example 2:
- Toss a fair coin 100 times, $Pr(X \geq 60 \cup X \leq 40)$
- $Pr(X \geq 60 \cup X \leq 40) = Pr(|X - 50| \geq 10) \leq \frac{25}{100} = \frac{1}{4}$

### Weak law of large numbers
- Let X_1, X_2, ... be a sequence of independent identically distributed (iid) RVs with mean $\mu$ and standard deviation $\sigma$. Consider $S_n = X_1 + ... + X_n$
- Then as $n \rightarrow \inf$, for all $\epsilon > 0$ the empirical average converges to $\mu$ in probability:
	- $\lim_{n \rightarrow \inf} Pr(|\frac{S_n}{n} - \mu| > \epsilon) = 0$
	- The empirical average converges to the mean as the sample size goes to infinity
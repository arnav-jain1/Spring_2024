#  Recurrence 

## Substitution Method

2 general steps:
	1. Guess the form of the solution (prove O and Ω seperately)
	2. Prove by induction
```
Ex: T(n) = 4T(n/2) + n
Guess: T(n) = O(n^3)
Prove T(n) <= cn^3 by induction

= 4c(n/2)^3 + n
= c/2*n^3 + n
smth idk 
```

## Recursion Tree Method
Recursion tree models running time of recursion
	Each node represents the cost of a certain problem
	Sum costs of each level then sum all per level costs to get total cost
	This method is unreliable though
![[Pasted image 20240131093259.png]]
This gives an intuitive solution which could still be wrong

## *Master method*
Used to solve problems like: T(n) = aT(n/b) +f(n) where a>0 and b > 1
### Case 1:
You check to see if $n^{\log _b\left(a\right)}$ is bigger by a polynomial factor than f(n)
If true then: T(n) = $\theta$ ($n^{\log _b\left(a\right)}$)
Another way is to see if $n^{\log _b\left(a\right)-\epsilon} >= f(n)$ where $\epsilon > 0$
Ex: T(n) = 4T(n/2) + n
 $f(n)= n$ and $=n^{\log _2\left(4\right)-\epsilon} = n^1$ so $T(n) = \theta(n^2))$ 

### Case 2:
If case 1 can't be applied then you take $f(n)=n^{\log _b\left(a\right)}$ and multiply it by $\log n$ 
For this to work $n^{\log _b\left(a\right)} == f(n)$ 
Another note is that if the equation is  $T(n) = 4T(n/2)+ n^2*log^k(x)$, $k>= 0$  
Ex: 
$T(n) = 4T(n/2)+ n^2$   
$n^{2-1}$ is not $<= n^2$ so case 1 does not apply. 
$n^{2}== f(n) = n^2$ so Case 2 applies

Instead $T(n) = \theta(n^2logn)$  

### Case 3: 
Case 3 applied when $n^{\log _b\left(a\right)} < f(n)$ then $\theta(n) = f(n)$
Ex: 
$T(n) = 4T(n/2)+ n^3$   
$=n^{\log _2\left(4\right)} = n^{2} < n^3$ so $\theta(n^3)$ 


## Binary Search
Find the middle
if middle is bigger, search left
else search right

$T(n) = 1*T(n) + \theta(1)$
$n^{\log _b\left(a\right)} = n^{\log _2\left(1\right)} = n^{0}= 1$  
$1 == f(n) = \theta(1)$ therefore we apply Master method case 2
Case 2: $T(n) = \theta(f(n)*\log n) = \theta(\log n)$  

## Strassen Method
Do more addition than multiplication
$T(n) = 7T\left(\frac{n}{2}\right) + \theta(n^2)$ 
$n^{\log _b\left(a\right)} = n^{\log _2\left(7\right)} = n^{2.807...}$ which is asymptotically better than $n^3$ 
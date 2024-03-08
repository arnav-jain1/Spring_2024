# Asymptotic

Asymptotic efficiency: worst case run-time with input size in the limit (going to infinity)
O Notation: Upper bound on the asymptotic effeciency of a function
    Function grows no faster than a certain rate
    Based on highest order
    (worst case)

Ω Notation: Lower bound on asymptotic effeciency of a function
    Function grows no slower than a certain rate
    Also based on higher order
    (best case)

θ Notation: Tight bound on asymptotic effeciency
    Grows percisely at a certain rate 
    Highest order term
    if O(f) == Ω(f) then θ(f)


Formal O notation: There exists constants so that 0 <= f(n) <= cg(n) where c is a constant for all n >= n0
    So if f(n) is 3n^3 - 5n + 7, O(n^3) also if f(n) = n then O(n^2) still holds
    Essentialy for O(g(n)), g(n) has to be same or higher degree than f(n)
![Alt text](image-5.png)

Formal Ω notation: There exists constants so that 0 <= cg(n) <= f(n) for all n >= (n0)
    So if f(n) is 3n^3 - 5n, Ω(n^3)
    Essentially for Ω(g(n)), g(n) has to be the same or lower degree than f(n)
![Alt text](image-6.png)

Formal θ notation: There exists constants so that θ <= c1g(n) <= f(n) <= c2g(n) for all n >= n0
![Alt text](image-7.png)


* THe big takeaway is that Θ is a precise bound. 
* O(nlogn) isn't neccessarily faster than O(n^2) because the O(n^2) can be Θ(n)

## o-notation

* o is <  while O is <=
* If o(n) means that the runtime is strickly slower than n while O(n) means it is slower than or equal to n
![Alt text](image-8.png)
* If f(n) = o(g(n)): g(n) > f(n)
  * If f(n) = O(g(n)): g(n) >= f(n)

## 𝜔-notation (Little omega)

* 𝜔 strict lower bound
* 𝜔 is > while Ω is >=
![Alt text](image-9.png)

* If f(n) = 𝜔(g(n)): f(n) > g(n)
  * If f(n) = Ω(g(n)): f(n) >= g(n)

## Summary
![Alt text](image-11.png)

## Properties

* Transitive property
  * If f(n) = O(g(n)) and g(n) = O(h(n)) then f(n) = O(g(n))
  * Applies to all 5 notations
* Symmetry
  * f(n) = θ(g(n)) if and only if g(n) = θ(f(n))
* Reflexive
  * f(n) = θ(f(n))
  * Works for all big notations
* Transpose symmetry
![Alt text](image-10.png)
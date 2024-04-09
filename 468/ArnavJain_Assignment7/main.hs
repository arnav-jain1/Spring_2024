{-
Author: Arnav Jain
Date: 3/31/23
Name: EECS 468 Assignment 7
Description: Haskell Functions
Inputs: None
Outputs: Outputs to questions given
Collaborators: Just me and the slides that were provided 
-}

-- PART 1


-- Replicate function that takes in an int and another var
replicate' :: Int -> a -> [a]
-- n is the amount of times x is the variable. This creates a new list containing x 1 to n times
replicate' n x = [x | _ <- [1..n]]



-- Perfects func that takes in an Int and outputs a list of ints
perfects :: Int -> [Int]
-- y is all of the numbers up to x. [d | d <- [1..y-1], y `mod` d == 0] gets all of the factors of y except itself. It is then summed and if it is equal to y, then it is added to the returned list
perfects x = [y | y <- [1..x], sum [d | d <- [1..y-1], y `mod` d == 0] == y]


-- Find func that takes in an array of (a,b) tuples (where a is a value that is comparable) and outputs a list of b
find :: Eq a => a -> [(a,b)] -> [b]
-- This function filters the input list (xs) so it only contains the tuples that include the input and then it gets the second element (b element) of all the remaining tuples
find x xs = map snd (filter(\(a,b) -> a == x) xs)


-- Positions function that takes in a comparable var and outputs a list of ints
positions :: Eq a => a -> [a] -> [Int]
-- The input ns is zipped with its index (from 0 to length -1) and then all of the indices where the value equals the input n are chosen
positions n ns = [i | (i,x) <- zip [0..(length ns) - 1] ns, x == n ]


-- scalar prod function takes 2 lists of Ints and outputs one Int
scalarproduct :: [Int] -> [Int] -> Int
-- the two lists xs and ys are zipped together and then multiplied to get a list of products. the list is then added
scalarproduct xs ys = sum [x*y | (x,y) <- zip xs ys]




-- PART 2


-- Base factorial function that takes in an Integer and outputs the product of all the numbers up to that Integer
factorial :: Integer -> Integer
factorial x = product [1..x]

-- Base combination function that outputs (x!)/(y!(x-y)!)
combination :: Integer -> Integer -> Integer
combination x y = factorial x `div` (factorial y * factorial (x - y))

-- Distinguish objects and boxes function which is just combination
distOdistB :: Integer -> Integer -> Integer
distOdistB x y = combination x y

-- Indistinguished objects and distinguished boxes that takes in 2 Integers and outputs the combination of (x+y-1) and x per slides
indisOdistB :: Integer -> Integer -> Integer
indisOdistB x y = combination (x+y-1) x


-- Stirling function from slides that takes in 2 Integers and outputs an Integer
stirling :: Integer -> Integer -> Integer
-- If both vars are 0 then return 1. If one but not both var is 0 then return 0. If both vars are same then return 1 and if x < y then return 0 (base cases)
stirling x y | x == 0 && y == 0 = 1
             | x == 0 || y == 0 = 0
             | x == y           = 1
             | x < y            = 0
            --  Otherwise, return y*recurse(x-1, y) + recurse(x-1, y-1) as per the slides
             | otherwise =       y * (stirling (x-1) y)  + stirling (x-1) (y-1)

-- Distinguished objects and indistinguished boxes function that takes in 2 Integers and outputs one Integer per slides
distOindisB :: Integer -> Integer -> Integer
-- if the second num is more than one, then: call stirling on both nums and add to recursive of x and y-1. Otherwise return 0 for the basecase
distOindisB x y | y >= 1 = (stirling x y) + (distOindisB x (y-1))
                | otherwise = 0

-- Indistinguishible objects and boxes: if x is 0 return 1. If second num is 0 or x is less than 1 return 0 (base case as per P function in slides)
indistOindistB :: Integer -> Integer -> Integer
indistOindistB x y | x == 0     = 1
                   | y == 0 || x < 1 = 0 
                --    Otherwise, recurse(x-y, y) + recurse(x, y-1)
                   | otherwise = (indistOindistB (x-y) y) + indistOindistB x (y-1)



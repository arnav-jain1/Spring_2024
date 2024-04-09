
sum' :: [Int] -> Int
sum' [] = 0
sum' (x:xs) = x + sum xs 

sumdown :: Int -> Int
sumdown 0   = 0
sumdown n   = n + sumdown (n-1)


mapandfilter :: (a -> b) -> (a -> Bool) -> [a] -> [b]
mapandfilter f p xs = map f (filter p xs)


data Tree a = Leaf a | Node (Tree a) (Tree a)

t1 = Leaf 1
t2 = Node (Leaf 1) (Leaf 2)
t3 = Node (Leaf 1) (Node (Leaf 2) (Leaf 3))
t4 = Node (Leaf 1) (Node (Leaf 2) (Node (Leaf 3) (Leaf 4)))

leaves :: Tree a -> Int
leaves (Leaf a) = 1
leaves (Node lhs rhs) = leaves (lhs) + leaves (rhs)

balanced :: Tree a -> Bool
balanced (Leaf a) = True
balanced (Node lhs rhs) = leaves lhs == leaves rhs
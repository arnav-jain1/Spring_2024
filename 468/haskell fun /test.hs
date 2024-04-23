import Data.List
import System.IO

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




type Grid = Matrix Char
type Matrix a = [Row a]
type Row a = [a]

boxsize :: Int
boxsize = 2
values :: [Char]
values = ['1'..'9']
empty :: Char -> Bool
empty = (== ' ')
single :: [a] -> Bool
single [_] = True
single _ = False

rows :: Matrix a -> [Row a]
rows m = m

cols :: Matrix a -> [Row a]
cols m = transpose m

boxs :: Matrix a -> [Row a]
boxs = unpack . map cols . pack
        where
            pack = split . map split
            split = chop boxsize
            unpack = map concat . concat


valid :: Grid -> Bool
valid g = all nodups (rows g) &&
          all nodups (cols g) &&
          all nodups (boxs g)
nodups :: Eq a => [a] -> Bool
nodups [] = True
nodups (x:xs) = not (elem x xs) && nodups xs

-- choices :: Grid ->  [Char]
-- choices = map choice v
--     where
--         choice v = if empty v then values else [v]

cp :: [[a]] -> [[a]]
cp [] = [[]]
cp (xs:xss) = [y:ys | y <- xs, ys <- cp xss]

chop :: Int -> [a] -> [[a]]
chop n [] = []
chop n xs = take n xs : chop n (drop n xs)

putStr' :: String -> IO ()
putStr' ns = sequence_ [putChar n | n <- ns]

putStrLn :: String -> IO ()
putStrLn ns = putStr' (ns ++ "\n")

getCh :: IO Char
getCh = do 
            hSetEcho stdin False
            x <- getChar
            hSetEcho stdin True
            return x

main :: IO ()
main = do
        putStr' "Password: "
        password <- getPass ""
        putStr' ("Length of input: " ++ show (length password) ++ "\n")

getPass :: String -> IO String
getPass pass = do
    letter <- getCh
    if letter /= '\n' then
        do
            putStr' ['*']
            getPass (pass ++ [letter])
    else 
        do
            putStr' ['\n']
            return pass

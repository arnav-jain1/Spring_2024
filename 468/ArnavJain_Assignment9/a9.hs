-- Warning ignores and inputs
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use when" #-}
import Data.Char (isDigit)
import Data.Char (digitToInt)



-- Set up the board
type Board = [Int]
initial :: Board
initial = [5,4,3,2,1]

-- Play function that takes in a board, int, and has a side effect
play :: Board -> Int -> IO ()
play b p= do 
    -- Print the board using display starting with index 0
    putStrLn "Board: "
    display b 0
    -- If the sum of the board is 0 then the game is over, switch the player to the one before this turn and print they are the winner
    if sum b == 0 then
        do
            putStrLn $ "Player " ++ show ((p `mod` 2) + 1) ++ " wins!"
            return ()
    else
        do
            -- Otherwise Print player, and get the info
            putStrLn $ "Player: " ++ show p     
            putStrLn $ "Enter row number: " 
            x <- getLine
            putStrLn $ "Enter how many stars would you like to remove?: "
            y <- getLine

            -- Make sure that all of the input is a digit, if it is not then tell the user to try again
            if not (all isDigit x && all isDigit y) then do
                putStrLn "Invalid move. Try again"
                play b p
            else do
                
 
                -- Convert the info to ints
                let row = (read x)-1
                let stars = read (y)


                -- If it is valid then call it again with the modified board and the player switched
                if valid b row stars then
                    play (modify b row stars) ((p `mod` 2) + 1)
                else do
                    -- Otherwise say it is invalid and recurse with same inputs
                    putStrLn "Invalid move. Try again"
                    play b p
            -- Then return to satisfy the output
            return ()






-- Display function that takes in the board and an index and prints to the screen
display :: Board -> Int -> IO ()
display b index = do
    -- First print the row number
    putStr ( show (index+1) ++ ": ")
    -- Then print the amount of '*'. Done by indexing using !!
    putStrLn (replicate (b!!index) '*')
    -- If the index is below 4, recurse otherwise return
    if index < (length b)-1 then
        display b (index+1)
        else return ()


-- Checks if a move is valid
valid :: Board -> Int -> Int -> Bool
-- If stars is negative, r is more than length of b or less than 0, it is invalid, b!!r indexes the board and gets the amount of stars, subtract the input from that and if it is less than o return true. \
-- If it is not any of these cases it is invalid
valid b r stars | stars <= 0 = False
                | r >= length b = False
                | r < 0 = False
                | b!!r - stars >= 0 = True
                | otherwise = False

-- Zip the board (amount of stars) and the index. Go through the board and if the index is the same as the input, subtract. otherwise keep it the same
modify :: Board -> Int -> Int -> Board
modify b r stars = [if i == r then x-stars else x | (x,i) <- zip b [0..4]]


-- Call the play function
nim :: IO ()
nim = play initial 0
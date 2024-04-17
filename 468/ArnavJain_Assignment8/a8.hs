{-
Author: Arnav Jain
Date: 4/14/23
Name: EECS 468 Assignment 8
Description: Expresion solver
Inputs: Expression
Outputs: Solution
Collaborators: Me, Aniketh Aatipamula, ChatGPT
-}
-- Telling IDE to ignore certain warnings
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Eta reduce" #-}

-- Expr datatype which takes in a double and is some operator with 2 of itself, a Negation with one of it self, or a Double. It is used as a showing and eq type
data Expr = Double
    | Add Expr Expr
    | Sub Expr Expr
    | Mul Expr Expr
    | Div Expr Expr
    | Mod Expr Expr
    | Exp Expr Expr
    | Neg Expr
    | Literal Double
    deriving(Show, Eq)

-- Simple func to see if a char is a space, if so return true else return false
isSpace :: Char -> Bool
isSpace ' ' = True
isSpace _ = False

-- Simple isDigit func that checks if the char is 0-9 or a decimal
isDigit :: Char -> Bool
isDigit '0' = True
isDigit '1' = True
isDigit '2' = True
isDigit '3' = True
isDigit '4' = True
isDigit '5' = True
isDigit '6' = True
isDigit '7' = True
isDigit '8' = True
isDigit '9' = True
isDigit '.' = True
isDigit _ = False

-- Evaluator function to evaluate the respective operation
eval :: Expr -> Double
eval (Literal a) = a
eval (Add l r) = eval l + eval r
eval (Sub l r) = eval l - eval r
eval (Mul l r) = eval l * eval r
eval (Div l r) = safeDiv (eval l) (eval r)
eval (Mod l r) =  moduloManual (eval l) (eval r)
eval (Exp l r) = eval l ** eval r
eval (Neg r) = - (eval r)

-- Function to do mods (takes in 2 doubles and outputs 1)
moduloManual :: Double -> Double -> Double
moduloManual x y
    -- if mod by 0 throw an error
    | y == 0 = error "Modulo by 0"
    -- If x == 0 return 0
    | x == 0 = 0
    -- If both are negative, call modulo manual on the positive version and make the answer negative
    | x < 0 && y < 0 = - moduloManual (-x) (-y)
    -- If only x is negative then add y to x and recurse
    | x < 0 = moduloManual (x+y) y
    -- If y is negative then same thing
    | y < 0 = moduloManual (x+y) (y)
    -- If x is more then y then subtract (both positive)
    | x > y = moduloManual (x - y) y
    -- Otherwise return x
    | otherwise = x

-- Safe division that throws an error when dividing by 0
safeDiv :: Double -> Double -> Double
safeDiv _ 0 = error "Dividing by 0"
safeDiv x y = x / y

-- Function that replaces ** with ^
replace :: String -> String
replace [] = []
replace ('*':'*':xs) = '^' : replace xs  -- When ** is found, replace with ^
replace (x:xs) = x : replace xs -- Otherwise continue to call it 

-- IsValid function that makes sure everything is valid
isValid :: String -> Bool
isValid [] = True
isValid (x:xs) = (isDigit x || isSpace x || isOp x) && isValid xs

-- IsOp function that makes sure everything is an operator
isOp :: Char -> Bool
isOp '*' = True
isOp '/' = True
isOp '-' = True
isOp '%' = True
isOp '+' = True
isOp '(' = True
isOp ')' = True
isOp _ = False


-- Parse binary Op function. Takes in a function that outputs an (expr, string) aka one of the parser functions or itself, char aka operator, a function that takes in two expressions and outputs another (aka Expr) to build the tree and the input string
-- In order to output a (expr, string) 
parseBinaryOp :: (String -> (Expr, String)) -> Char -> (Expr -> Expr -> Expr) -> String -> (Expr, String)
-- The 4 inputs are next, op, constructor, and input
parseBinaryOp next op constructor input =
    -- Temporary vars 'first' is the first output of next(input) and 'rest' is the rest
    let (first, rest) = next input
    in case rest of
        -- If there are 2+ elements in rest then recurse otherwise return first,rest
        (c:cs) | c == op -> let (second, finalRest) = parseBinaryOp next op constructor cs in (constructor first second, finalRest)
        otherwise -> (first, rest)





-- Parse addition function that takes in a string and outputs expr, string
parseAdd :: String -> (Expr, String)
-- Call the parseBinaryOp with parseSub function because it has more/same presedence, the constructor '+', the Expr Add, and the input
parseAdd input = parseBinaryOp parseSub '+' Add input

-- Same thing for all but precedence keeps getting higher
parseSub :: String -> (Expr, String)
parseSub input = parseBinaryOp parseMod '-' Sub input

parseMod :: String -> (Expr, String)
parseMod input = parseBinaryOp parseMul '%' Mod input

parseMul :: String -> (Expr, String)
parseMul input = parseBinaryOp parseDiv '*' Mul input

parseDiv :: String -> (Expr, String)
parseDiv input = parseBinaryOp parsePow '/' Div input




parsePow :: String -> (Expr, String)
parsePow input = parseBinaryOp parseNeg '^' Exp input

-- Once it gets to negation, it takes in the same input
parseNeg :: String -> (Expr, String)
-- It checks to see if the first element is a negative, if it is then call parseFactor on the input and output Neg of the expr (the Expr in the tree) and rest
parseNeg ('-':input) = let (expr, rest) = parseFactor input in (Neg expr, rest)
-- Otherwise skip essentially
parseNeg input = parseFactor input



-- ParseFactor for parenthesis 
parseFactor :: String -> (Expr, String)
-- If the input is a (
parseFactor ('(':input) =
    -- Then call parseExpr for the rest until ). If there is no ) then throw an error
    let (expr, rest) = parse input  -- This treats the stuff inside () as its own thing and starts the parsing of that
    in case rest of
         ')' : more -> (expr, more)  -- Goes through rest to see if there is a ). More is there to get everything after the )
         _ -> error "Missing closing parenthesis"  -- Throw an error if there is no ) 
-- Otherwise
parseFactor input =
    -- split the string into two parts. Number (including . by checking if the char is a digit) and everything else
    let (num, rest) = span isDigit input
    -- then makes sure the number is not nothing if it is, throw en error
    in if not (null num)
       then (Literal (read num :: Double), rest)
       else error "Missing a number or some input error like closed parenthesis before open, dangling number/operator"

-- parser function that takes in a string and outputs expr and string
parse :: String -> (Expr, String)
parse input =
    -- Start going down the parsers by calling parseAdd on the input without any spaces 
    let (result, rest) = parseAdd (filter (not . isSpace) input)
    in (result, rest)

-- Function that starts the eval and outputs the value
evaluate :: String -> Double
-- Eval function 
evaluate input
    | null input = error "Empty evaluate"
    -- If it is valid,then replace input and parse it
    | isValid input = case parse (replace input) of
        -- If the parse function returns an expr and an empty string, it worked and you can evaluate it
        (expr, "") -> eval expr
        -- If it returned some other stuff, that means there is stuff that didn't get parsed for some reason so throw an error
        (_, rest) -> error $ "Unparsed input remaining: " ++ rest
    -- If it is not valid (other chars) throw an error
    | otherwise = error "Invalid input"
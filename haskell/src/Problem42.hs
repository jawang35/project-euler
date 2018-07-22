{- |
Problem 42 - Coded Triangle Numbers

The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
-}

module Problem42
( answer
, isTriangleWord
) where

import System.IO (readFile)
import Data.Char (ord)
import Data.List.Split (splitOn)
import Config (assetsPath)
import Helpers.Numbers (isTriangular)
import Helpers.Runtime (printAnswerAndElapsedTime)

charValue :: Char -> Int
charValue char =
    ord char - offset
    where offset = ord 'A' - 1

wordValue :: String -> Int
wordValue = sum . map charValue

isTriangleWord :: String -> Bool
isTriangleWord = isTriangular . wordValue

answer :: IO Int
answer = do
    contents <- readFile $ assetsPath ++ "/problem42/words.txt"
    let codes = map (filter (/= '"')) $ splitOn "," contents
    return $ length $ filter isTriangleWord codes

main = do
    value <- answer
    printAnswerAndElapsedTime value

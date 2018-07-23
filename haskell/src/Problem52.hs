{- |
Problem 52 - Permuted Multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
-}

module Problem52
( answer
, sameDigits
) where

import Data.Digits (digits)
import Data.List (sort)
import Helpers.Runtime (printAnswerAndElapsedTime)

sameDigits :: [Int] -> Bool
sameDigits []     = True
sameDigits (x:xs) =
    all ((==) sortedDigits . sort . digits 10) xs
    where sortedDigits = sort $ digits 10 x

answer :: Int
answer = head . head $ filter sameDigits [[x, 2 * x, 3 * x, 4 * x, 5 * x, 6 * x] | x <- [1..]]

main = printAnswerAndElapsedTime answer

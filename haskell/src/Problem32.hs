{- |
Problem 32 - Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
-}

module Problem32
( answer
, pandigitalProducts
) where

import Data.List (nub, nubBy, sort)
import Helpers.Runtime (printAnswerAndElapsedTime)

isPandigitalProduct :: Int -> Int -> Bool
isPandigitalProduct x y = (sort $ show x ++ show y ++ show (x * y)) == "123456789"

uniqueDigits :: Int -> Bool
uniqueDigits number = (length $ nub numString) == length numString
    where numString = show number

pandigitalProducts :: [(Int, Int, Int)]
pandigitalProducts =
    nubBy (\(_, _, p1) (_, _, p2) -> p1 == p2) [ (x, y, x * y)
                                               | x <- takeWhile (<= 99) uniqueDigitNumbers
                                               , y <- takeWhile (<= 4999) uniqueDigitNumbers
                                               , isPandigitalProduct x y
                                               ]
    where uniqueDigitNumbers = filter uniqueDigits [2..]

answer :: Int
answer = sum $ map (\(_, _, p) -> p) pandigitalProducts

main = printAnswerAndElapsedTime answer

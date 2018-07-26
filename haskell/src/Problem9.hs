{- |
Problem 9 - Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
-}

module Problem9
( answer
, productSpecialPythagoreanTriplet
) where

import Helpers.Runtime (printAnswerAndElapsedTime)

isPythagorean :: (Int, Int, Int) -> Bool
isPythagorean (a, b, c) = a^2 + b^2 == c^2

productFirstPythagoreanTriplet :: [(Int, Int, Int)] -> Int
productFirstPythagoreanTriplet [] = 0
productFirstPythagoreanTriplet (x:_) = tripletProduct x
    where tripletProduct (a, b, c) = a * b * c

productSpecialPythagoreanTriplet :: Int -> Int
productSpecialPythagoreanTriplet perimeter =
    productFirstPythagoreanTriplet specialPythagoreanTriplets
    where possibleTriplets = [(a, b, perimeter - a - b) | a <- [1..(perimeter - 2)], b <- [a..(perimeter - a - 1)]]
          specialPythagoreanTriplets = filter isPythagorean possibleTriplets

answer :: Int
answer = productSpecialPythagoreanTriplet 1000

main = printAnswerAndElapsedTime answer

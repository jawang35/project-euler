{- |
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
-}

module Problem3
( largestPrimeFactor
, answer
) where

import Helpers.Numbers (primeDivisors)

largestPrimeFactor :: Integer -> Integer
largestPrimeFactor = maximum . primeDivisors

answer = largestPrimeFactor 600851475143

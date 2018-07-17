{- |
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
-}

module Problem3
( answer
, largestPrimeFactor
) where

import Math.NumberTheory.Primes.Factorisation (factorise)
import Helpers.Runtime (printAnswerAndElapsedTime)

largestPrimeFactor :: Integer -> Integer
largestPrimeFactor = maximum . map fst . factorise

answer :: Integer
answer = largestPrimeFactor 600851475143

main = printAnswerAndElapsedTime answer

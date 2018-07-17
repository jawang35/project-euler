{- |
Problem 47 - Distinct Prime Factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
-}

module Problem47
( answer
) where

import Data.List (elemIndex, zip4)
import Data.Maybe (fromJust)
import Math.NumberTheory.Primes.Factorisation (factorise)
import Helpers.Runtime (printAnswerAndElapsedTime)

answer =
    1 + (fromJust $ elemIndex (4, 4, 4, 4) $ zip4 primeFactorCounts (drop 1 primeFactorCounts) (drop 2 primeFactorCounts) (drop 3 primeFactorCounts))
    where primeFactorCounts = map (length . factorise) [1..]

main = printAnswerAndElapsedTime answer

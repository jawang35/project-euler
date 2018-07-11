{- |
Problem 10 - Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
-}

module Problem10
( answer
) where

import Helpers.Numbers (primes)
import Helpers.Runtime (printAnswerAndElapsedTime)

answer :: Int
answer = sum $ takeWhile (<2000000) primes

main = printAnswerAndElapsedTime answer

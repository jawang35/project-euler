{- |
Problem 7 - 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
-}

module Problem7
( answer
, nthPrimeNumber
) where

import Math.NumberTheory.Primes.Sieve (primes)
import Helpers.Runtime (printAnswerAndElapsedTime)

nthPrimeNumber :: Int -> Integer
nthPrimeNumber number =
    primes !! (number - 1)

answer :: Integer
answer = nthPrimeNumber 10001

main = printAnswerAndElapsedTime answer

{- |
Problem 41 - Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
-}

module Problem41
( answer
) where

import Data.Digits (digits)
import Data.List (find, sort)
import Data.Maybe (fromJust)
import Helpers.Numbers (primes)
import Helpers.Runtime (printAnswerAndElapsedTime)

isPandigital :: Int -> Bool
isPandigital number = sort numberDigits == take (length numberDigits) [1..]
    where numberDigits = digits 10 number

answer :: Int
answer = fromJust $ find isPandigital $ reverse $ takeWhile (<= 7654321) primes

main = printAnswerAndElapsedTime answer

{- |
Problem 20 - Factorial Digit Sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
-}

module Problem20
( answer
, sumFactorialDigits
) where

import Data.Digits (digits)
import Helpers.Runtime (printAnswerAndElapsedTime)

sumFactorialDigits :: Integer -> Integer
sumFactorialDigits n = sum $ digits 10 $ product [1..n]

answer :: Integer
answer = sumFactorialDigits 100

main = printAnswerAndElapsedTime answer

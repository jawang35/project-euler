{- |
Problem 34 - Digit Factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
-}

module Problem34
( answer
) where

import Data.Char (digitToInt)
import Helpers.Runtime (printAnswerAndElapsedTime)

sumDigitFactorial :: Int -> Int
sumDigitFactorial =
    sum . map (factorial . digitToInt) . show
    where factorial = product . (flip take [1..])

answer :: Int
-- 10000000 is an analytical upper bound since 9999999 > 7 * 9!
answer = sum $ filter (\n -> n == sumDigitFactorial n) [10..50000]

main = printAnswerAndElapsedTime answer

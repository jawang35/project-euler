{- |
Problem 23 - Non-abundant Sums

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
-}

module Problem23
( answer
, sumNonAbundantSums
) where

import Data.IntSet (fromList, toList)
import Helpers.Numbers (properDivisors)
import Helpers.Runtime (printAnswerAndElapsedTime)

nub' :: [Int] -> [Int]
nub' = toList . fromList

sumNonAbundantSums :: Int
sumNonAbundantSums =
    sum [1..28123] - sum abundantSums
    where abundantNumbers = filter (\n -> sum (properDivisors n) > n) [12..28123]
          abundantSums    = nub' [total | a <- abundantNumbers
                                        , b <- abundantNumbers
                                        , a <= b
                                        , let total = a + b
                                        , total <= 28123
                                 ]

answer :: Int
answer = sumNonAbundantSums

main = printAnswerAndElapsedTime answer

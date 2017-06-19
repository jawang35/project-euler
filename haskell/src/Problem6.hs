{- |
Problem 6 - Sum Square Difference

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
-}

module Problem6
( answer
, sumSquareDifference
) where

import Helpers.Runtime (printAnswerAndElapsedTime)

sumSquareDifference :: Integer -> Integer
sumSquareDifference maximum =
    squareOfSums - sumOfSquares
    where naturalNumbers = [1..maximum]
          squareOfSums = (sum naturalNumbers) ^ 2
          sumOfSquares = sum $ map (^2) naturalNumbers

answer = sumSquareDifference 100

main = printAnswerAndElapsedTime answer

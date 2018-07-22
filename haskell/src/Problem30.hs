{- |
Problem 30 - Digit Fifth Powers

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
-}

module Problem30
( answer
, sumPowersOfDigits
) where

import Data.Digits (digits, unDigits)
import Helpers.Runtime (printAnswerAndElapsedTime)

isSumPowerOfDigits :: Int -> Integer -> Bool
isSumPowerOfDigits power number =
    number == toInteger sumPowerOfDigits
    where sumPowerOfDigits = sum $ map (^power) $ digits 10 number

sumPowersOfDigits :: Int -> Integer
sumPowersOfDigits power =
    sum $ filter (isSumPowerOfDigits power) $ take largest [10..]
    where largestNumbers     = map (unDigits 10 . flip replicate 9) [1..]
          largestSumOfPowers = map (* (9^power)) [1..]
          (_, largest)       = last
                               $ takeWhile (uncurry (<))
                               $ zip largestNumbers largestSumOfPowers

answer :: Integer
answer = sumPowersOfDigits 5

main = printAnswerAndElapsedTime answer

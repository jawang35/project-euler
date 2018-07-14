{- |
Problem 43 - Sub-string Divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note
the following:

d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
-}

module Problem43
( answer
) where

import Data.Digits (digits, unDigits)
import Data.List ((\\), nub)
import Helpers.Runtime (printAnswerAndElapsedTime)

hasUniqueDigits :: Int -> Bool
hasUniqueDigits number =
    (length $ nub numberDigits) == length numberDigits
    where numberDigits = show number

uniqueDigitMultiples :: Int -> [Int]
uniqueDigitMultiples factor = filter hasUniqueDigits $ takeWhile (<1000) $ dropWhile (<100) [factor, (factor * 2)..]

answer :: Int
answer =
    sum $ map (unDigits 10) $ foldl (\numbers factor -> filter ((== 0) . (`mod` factor) . (unDigits 10) . (take 3)) [digit:number | number <- numbers, digit <- pandigitalDigits \\ number]) startingValue [13, 11, 7, 5, 3, 2, 1]
    where startingValue    = map (digits 10) $ uniqueDigitMultiples 17
          pandigitalDigits = [0..9]

main = printAnswerAndElapsedTime answer

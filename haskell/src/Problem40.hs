{- |
Problem 40 - Champernowne's Constant

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
-}

module Problem40
( answer
) where

import Data.Char (digitToInt)
import Helpers.Runtime (printAnswerAndElapsedTime)

answer :: Int
answer =
    product [ fractionalPart !! 0
            , fractionalPart !! 9
            , fractionalPart !! 99
            , fractionalPart !! 999
            , fractionalPart !! 9999
            , fractionalPart !! 99999
            , fractionalPart !! 999999
            ]
    where fractionalPart = map digitToInt $ concat $ map show [1..]

main = printAnswerAndElapsedTime answer

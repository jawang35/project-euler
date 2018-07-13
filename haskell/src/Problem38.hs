{- |
Problem 38 - Pandigital Multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
-}

module Problem38
( answer
) where

import Data.List (sort)
import Data.Digits (digits, unDigits)
import Helpers.Runtime (printAnswerAndElapsedTime)

isPandigital :: Int -> Bool
isPandigital = (== "123456789") . sort . show

concatenatedProduct :: Int -> Int
concatenatedProduct number =
    unDigits 10 $ take 9 $ concat $ map ((digits 10) . (* number)) [1..]

concatenatedProducts :: [Int]
concatenatedProducts = filter isPandigital $ map concatenatedProduct [1..9876]

answer :: Int
answer = maximum concatenatedProducts

main = printAnswerAndElapsedTime answer

{- |
Problem 1 - Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

'''
Computed by Hand:
Use the formula 1 + 2 + ... + n = n * (n + 1) / 2
(3 + 6 + ... + 999) + (5 + 10 + ... + 995) - (15 + 30 + ... + 990)
= 3 * (1 + 2 + ... + 333) + 5 * (1 + 2 + ... + 199) - 15 * (1 + 2 + ... + 66)
= (3 * 333 * 334 / 2) + (5 * 199 * 200 / 2) - (15 * 66 * 67 / 2)
= 166833 + 99500 - 33165
= 233168<Paste>
-}

module Problem1
( answer
, sumMultiplesOf3And5
) where

import Helpers.Runtime (printAnswerAndElapsedTime)

sumMultiplesOf3And5 :: Int -> Int
sumMultiplesOf3And5 maximum =
    sum $ filter multipleOf3Or5 $ init [1..maximum]
    where multipleOf3Or5 number = number `mod` 3 == 0 || number `mod` 5 == 0

answer :: Int
answer = sumMultiplesOf3And5 1000

main = printAnswerAndElapsedTime answer

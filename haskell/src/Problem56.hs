{- |
Problem 56 - Powerful Digit Sum

A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the
maximum digital sum?
-}

module Problem56
( answer
) where

import Data.Digits (digits)
import Helpers.Runtime (printAnswerAndElapsedTime)

answer :: Integer
answer = maximum [sum . digits 10 $ a ^ b | a <- [1..99], b <- [1..99]]

main = printAnswerAndElapsedTime answer

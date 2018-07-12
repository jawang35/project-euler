{- |
Problem 16 - Power Digit Sum

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
-}

module Problem16
( answer
) where

import Data.Digits (digits)
import Helpers.Runtime (printAnswerAndElapsedTime)

answer :: Integer
answer = sum $ digits 10 $ 2^1000

main = printAnswerAndElapsedTime answer

{- |
Problem 48 - Self Powers

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
-}

module Problem48
( answer
, lastTenDigits
) where

import Data.Digits (digits, unDigits)
import Helpers.Runtime (printAnswerAndElapsedTime)

lastTenDigits :: Integer -> Integer
lastTenDigits = unDigits 10 . reverse . take 10 . reverse . digits 10

answer :: Integer
answer = lastTenDigits . sum $ map (\n -> n^n) [1..1000]

main = printAnswerAndElapsedTime answer

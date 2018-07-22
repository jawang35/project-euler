{- |
Problem 36 - Double-base Palindromes

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
-}

module Problem36
( answer
) where

import Data.Digits (digits)
import Helpers.Lists (isPalindrome)
import Helpers.Runtime (printAnswerAndElapsedTime)

answer :: Int
answer =
    sum $ filter (\n -> isPalindrome (digits 10 n) && isPalindrome (digits 2 n)) [1..999999]

main = printAnswerAndElapsedTime answer

{- |
Problem 4 - Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
-}

module Problem4
( answer
, largestPalindromeProduct
) where

import Helpers.Lists (isPalindrome)
import Helpers.Runtime (printAnswerAndElapsedTime)

largestPalindromeProduct :: Int -> Int -> Int
largestPalindromeProduct min max =
    maximum $ filter (isPalindrome . show) products
    where products = [n * m | n <- [min..max], m <- [n..max]]

answer :: Int
answer = largestPalindromeProduct 100 1000

main = printAnswerAndElapsedTime answer

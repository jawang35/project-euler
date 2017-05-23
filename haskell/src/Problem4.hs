{- |
Problem 4 - Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
-}

module Problem4
( largestPalindromeProduct
, answer
) where

import Helpers.Strings (isPalindrome)

largestPalindromeProduct :: Integer -> Integer -> Integer
largestPalindromeProduct min max =
    maximum $ filter (\n -> isPalindrome $ show n) products
    where products = [n * m | n <- [min..max], m <- [n..max]]

answer = largestPalindromeProduct 100 1000

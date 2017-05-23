module Helpers.Strings
( isPalindrome
) where

isPalindrome :: String -> Bool
isPalindrome string = string == reverse string

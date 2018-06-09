{- |
Problem 14 - Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
-}

module Problem14
( answer
, longestCollatzSequence
) where

import Data.List (elemIndex)
import Data.Maybe (fromJust)
import Helpers.Runtime (printAnswerAndElapsedTime)

collatzSequence :: Int -> [Int]
collatzSequence 1 = [1]
collatzSequence number =
    number:(collatzSequence next)
    where
        next
            | (number `mod` 2 == 0) = number `div` 2
            | otherwise           = 3 * number + 1

longestCollatzSequence :: Int -> Int
longestCollatzSequence limit =
    fromJust (elemIndex longestSequenceLength sequenceLengths) + 1
    where sequenceLengths       = map (length . collatzSequence) [1..limit]
          longestSequenceLength = maximum sequenceLengths

answer :: Int
answer = longestCollatzSequence 999999

main = printAnswerAndElapsedTime answer

{- |
Problem 26 - Reciprocal Cycles

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	 = 0.5
1/3	 = 0.(3)
1/4	 = 0.25
1/5	 = 0.2
1/6	 = 0.1(6)
1/7	 = 0.(142857)
1/8	 = 0.125
1/9	 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
-}

module Problem26
( answer
, recurringCycleLength
) where

import Data.List (maximumBy)
import Data.Map.Strict (Map)
import qualified Data.Map.Strict as Map
import Helpers.Runtime (printAnswerAndElapsedTime)

quotientDigits :: (Int, Int) -> [(Int, Int)]
quotientDigits (numerator, denominator)
    | numerator == 0 = []
    | otherwise      = (quotient, remainder):quotientDigits (remainder * 10, denominator)
    where
        quotient  = numerator `div` denominator
        remainder = numerator `mod` denominator

findCycle :: Map Int Int -> [(Int, (Int, Int))] -> Int
findCycle _ []                              = 0
findCycle digitMap ((i, (_, remainder)):ds) =
    if Map.member remainder digitMap
        then i - (digitMap Map.! remainder)
        else findCycle (Map.insert remainder i digitMap) ds

recurringCycleLength :: (Int, Int) -> Int
recurringCycleLength fraction@(numerator, denominator) =
    findCycle digitMap $ zip [1..] decimals
    where decimals = tail $ quotientDigits fraction
          digitMap = Map.singleton 0 0

answer :: Int
answer =
    fst $ maximumBy (\(_, x) (_, y) -> compare x y)
        $ zip [1..]
        $ take 999
        $ map (curry recurringCycleLength 1) [1..]

main = printAnswerAndElapsedTime answer

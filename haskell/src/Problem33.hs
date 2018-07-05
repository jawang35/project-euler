{- |
Problem 33 - Digit Cancelling Fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
-}

module Problem33
( answer
, badSimplification
) where

import Data.List (intersect)
import Data.Ratio ((%), denominator)
import Helpers.Runtime (printAnswerAndElapsedTime)

removeItem :: (Eq a) => a -> [a] -> [a]
removeItem _ [] = []
removeItem item (x:xs)
    | x == item = xs
    | otherwise = x:(removeItem item xs)

removeItems :: (Eq a) => [a] -> [a] -> [a]
removeItems [] ys     = ys
removeItems (x:xs) ys =
    removeItems xs $ removeItem x ys

badSimplification :: Int -> Int -> (Int, Int)
badSimplification numerator denominator =
    (simplifiedNumerator, simplifiedDenominator)
    where commonDigits           = intersect (show numerator) (show denominator)
          simplifiedNumeratorS   = removeItems commonDigits $ show numerator
          simplifiedDenominatorS = removeItems commonDigits $ show denominator
          simplifiedNumerator    = if simplifiedNumeratorS == "" then 1 else read simplifiedNumeratorS
          simplifiedDenominator  = if simplifiedDenominatorS == "" then 1 else read simplifiedDenominatorS

answer :: Int
answer =
    denominator $ product
        [ (n % d)
        | n <- [1..99]
        , d <- [1..99]
        , n < d
        , n `mod` 10 /= 0 || d `mod` 10 /= 0
        , let (bsn, bsd) = badSimplification n d in
            bsd /= 0
            && bsn /= n
            && (n % d) == (bsn % bsd)
        ]

main = printAnswerAndElapsedTime answer

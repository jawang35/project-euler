{- |
Problem 57 - Square Root Convergents

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
-}

module Problem57
( answer
, isImproper
, sqrt2Fractions
) where

import Data.Ratio (Ratio, (%), denominator, numerator)
import Helpers.Runtime (printAnswerAndElapsedTime)

isImproper :: Ratio Integer -> Bool
isImproper fraction =
    (length . show $ numerator fraction) > (length . show $ denominator fraction)

sqrt2Fractions :: [Ratio Integer]
sqrt2Fractions =
    scanl (nextIteration) (3 % 2) [1..]
    where nextIteration f _ = let f' = 1 + f in 1 + denominator f' % numerator f'

answer :: Int
answer = length . filter isImproper $ take 1000 sqrt2Fractions

main = printAnswerAndElapsedTime answer

{- |
Problem 37 - Truncatable Primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
-}

module Problem37
( answer
) where

import Data.Digits (digits, unDigits)
import Data.List (nub)
import Helpers.Numbers (isPrime)
import Helpers.Runtime (printAnswerAndElapsedTime)

truncatablePrimes :: Int -> Bool
truncatablePrimes number =
    isPrime number && all isPrime (leftTruncations ++ rightTruncations)
    where numberDigits             = digits 10 number
          size                     = (length numberDigits) - 1
          leftTruncations          = nub $ map ((unDigits 10) . (flip drop numberDigits)) $ take size [1..]
          rightTruncations         = nub $ map ((unDigits 10) . (flip take numberDigits)) $ take size [1..]

answer = sum $ take 11 $ filter truncatablePrimes [11..]

main = printAnswerAndElapsedTime answer

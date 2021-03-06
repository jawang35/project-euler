{- |
Problem 21 - Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
-}

module Problem21
( answer
, sumAmicableNumbers
) where

import qualified Data.Map.Strict as Map
import qualified Data.Set as Set
import Helpers.Numbers (properDivisors)
import Helpers.Runtime (printAnswerAndElapsedTime)

sumAmicableNumbers :: Int -> Int
sumAmicableNumbers maximum =
    sum $ map snd amicablePairs
    where numbers            = [1..maximum]
          divisorSums        = map (\n -> (n, sum $ properDivisors n)) numbers
          divisorSumsMap     = Map.fromList divisorSums
          isAmicable (n, ds) = ds /= 0
                            && ds < maximum
                            && ds /= n
                            && (divisorSumsMap Map.! ds == n)
          amicablePairs      = filter isAmicable divisorSums

answer :: Int
answer = sumAmicableNumbers 10000

main = printAnswerAndElapsedTime answer

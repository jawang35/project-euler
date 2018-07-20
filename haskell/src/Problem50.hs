{- |
Problem 50 - Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
-}

module Problem50
( answer
, longestConsecutivePrimeSum
) where

import Data.List (maximumBy)
import Data.Maybe (fromJust)
import qualified Data.Set as Set
import Math.NumberTheory.Primes.Sieve (primes)
import Helpers.Runtime (printAnswerAndElapsedTime)

longestConsecutivePrimeSum :: Integer -> (Int, Integer)
longestConsecutivePrimeSum limit =
    maximumBy (\(x, _) (y, _) -> compare x y) . map fromJust . takeWhile (\x -> x /= Nothing && (fst . fromJust) x /= 1) $ map longestSumStartingAt [1..]
    where validPrimes                = takeWhile (< limit) primes
          validPrimeSet              = Set.fromList validPrimes
          longestSumStartingAt index = let sums = filter (flip Set.member validPrimeSet . snd) . zip [1..] . takeWhile (< limit) $ map (sum . (flip take $ drop index validPrimes)) [1..]
                                       in if sums /= [] then Just $ last sums else Nothing

answer :: Integer
answer = snd $ longestConsecutivePrimeSum 1000000

main = printAnswerAndElapsedTime answer

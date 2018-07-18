{- |
Problem 49 - Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing
sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
-}

module Problem49
( answer
, primePermutations
, threeNumberSequence
) where

import Data.Digits (digits, unDigits)
import Data.List (nub, permutations, sort)
import Data.Maybe (fromJust)
import Data.Set (Set)
import qualified Data.Set as Set
import Math.NumberTheory.Primes.Sieve (primes)
import Helpers.Runtime (printAnswerAndElapsedTime)

primePermutations :: Integer -> [Integer]
primePermutations prime =
    nub . sort . filter (flip Set.member fourDigitPrimeSet) . map (unDigits 10) . permutations $ digits 10 prime

fourDigitPrimes :: [Integer]
fourDigitPrimes = takeWhile (<10000) $ dropWhile (< 1000) primes

fourDigitPrimeSet :: Set Integer
fourDigitPrimeSet = Set.fromList fourDigitPrimes

threeNumberSequence :: [Integer] -> Maybe (Integer, Integer, Integer)
threeNumberSequence sortedNumbers =
    if sequences /= [] then Just $ head sequences else Nothing
    where sequences = [ (a, b, b + (b - a))
                      | a <- sortedNumbers
                      , b <- dropWhile (<= a) sortedNumbers
                      , b + (b - a) `elem` sortedNumbers
                      ]

answer :: Integer
answer =
    unDigits 10 $ digits 10 first ++ digits 10 second ++ digits 10 third
    where (first, second, third) = head $ filter (/= (1487,4817,8147))
                                        $ map (fromJust)
                                        $ filter (/= Nothing)
                                        $ map threeNumberSequence
                                        $ map primePermutations fourDigitPrimes

main = printAnswerAndElapsedTime answer

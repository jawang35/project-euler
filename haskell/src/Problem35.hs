{- |
Problem 35 - Circular Primes

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
-}

module Problem35
( answer
) where

import qualified Data.Set as Set
import Helpers.Numbers (primes)
import Helpers.Runtime (printAnswerAndElapsedTime)

rotate :: Int -> [Int]
rotate number =
    map (\i -> read $ take size $ drop i $ cycle numberString) $ take size [1..]
    where numberString = show number
          size         = length numberString

circularPrimes :: Int -> [Int]
circularPrimes limit =
    filter isCircularPrime validPrimes
    where validPrimes       = takeWhile (<limit) primes
          primeSet          = Set.fromList $ validPrimes
          isCircularPrime p = let rotations = rotate p in rotations == filter (\n -> Set.member n primeSet) rotations

answer :: Int
answer = length $ circularPrimes 1000000

main = printAnswerAndElapsedTime answer

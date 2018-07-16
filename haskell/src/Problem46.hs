{- |
Problem 46 - Goldbach's Other Conjecture

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
-}

module Problem46
( answer
) where

import Data.List ((\\))
import Helpers.Numbers (primes, isPrime)
import Helpers.Runtime (printAnswerAndElapsedTime)

isInteger :: (RealFrac a) => a -> Bool
isInteger number =
    number == (fromIntegral $ round number)

isSquare :: (RealFrac a, Floating a) => a -> Bool
isSquare number =
    isInteger number && isInteger root
    where root = sqrt number

isGoldbach :: Int -> Bool
isGoldbach number =
    any (\p -> isSquare $ (fromIntegral ((number - p)) / 2)) $ takeWhile (< number) primes

answer :: Int
answer = head $ filter (\n -> odd n && not (isPrime n) && not (isGoldbach n)) [2..]

main = printAnswerAndElapsedTime answer
